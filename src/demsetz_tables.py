"""Rebuild Demsetz (1973), Tables 1 to 4, from IRS corporate tax returns and Census concentration ratios.

Demsetz split each manufacturing industry's corporations into four asset-size classes, computed the
accounting rate of return (profit plus interest) / total assets for each class, and asked whether the
gap between the largest and smallest firms widens as industry concentration rises (efficiency) or
whether the smallest firms also earn more in concentrated industries (collusion).

This script does the same with the IRS Corporation Source Book (the same IRS series Demsetz used for
1963; the IRS published its last industry-by-asset-size edition for tax year 2013) and the Census
Bureau's Economic Census four-firm concentration ratios. The primary pairing is tax year 2012 with
the 2012 Economic Census, mirroring Demsetz's same-year pairing of 1963 returns with 1963
concentration. Tax year 2013 (with 2012 concentration) and 2007 (with 2007 concentration) are rerun
as checks, and the 2007-to-2012 change in concentration stands in for his 1963-to-1967 change.

All inputs are committed in data/raw/. Usage, from the repository root:
    python src/demsetz_tables.py
Writes results/industries_<year>.csv, results/demsetz_tables.csv, results/regressions.csv,
results/paper_tables.csv, results/size_thresholds.csv and two figures.
"""

import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

# The IRS documentation is an old-format .xls; pandas reads it with xlrd and warns that the engine is deprecated.
warnings.filterwarnings("ignore", message="The xlrd engine")

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
OUT = ROOT / "results"

# Demsetz's size classes in 1963 dollars: R1 < $0.5M, R2 $0.5-5M, R3 $5-50M, R4 > $50M (paper, p. 5).
DEMSETZ_EDGES_1963 = [500, 5_000, 50_000]  # thousands of dollars
# Lower edges of the IRS Source Book asset classes AC 3..13, thousands of dollars (flat-file documentation).
IRS_AC_LOWER = {3: 1, 4: 500, 5: 1_000, 6: 5_000, 7: 10_000, 8: 25_000, 9: 50_000, 10: 100_000,
                11: 250_000, 12: 500_000, 13: 2_500_000}
# Demsetz's concentration classes (Tables 1 and 2); "under 10" added because modern data reach below 10%.
CR_BINS = [0, 10, 20, 30, 40, 50, 60, 101]
CR_LABELS = ["under 10%", "10-20%", "20-30%", "30-40%", "40-50%", "50-60%", "over 60%"]

# IRS Source Book manufacturing minor industries and the NAICS codes each one covers, read from the
# industry titles in the Source Book documentation (codes ending in 5 combine neighbouring industries).
IRS_TO_NAICS = {
    311115: ["3111", "3112"], 311300: ["3113"], 311400: ["3114"], 311500: ["3115"],
    311615: ["3116", "3117"], 311800: ["3118"], 311900: ["3119"],
    312110: ["31211"], 312120: ["31212"], 312135: ["31213", "31214"], 312200: ["3122"],
    313000: ["313"], 314000: ["314"], 315100: ["3151"], 315215: ["3152"], 315990: ["3159"],
    316: ["316"], 321: ["321"], 322100: ["3221"], 322200: ["3222"], 323100: ["3231"],
    324110: ["32411"], 324125: ["32412", "32419"],
    325100: ["3251"], 325200: ["3252"], 325410: ["3254"], 325500: ["3255"], 325600: ["3256"],
    325905: ["3253", "3259"], 326100: ["3261"], 326200: ["3262"],
    327105: ["3271", "3279"], 327210: ["3272"], 327305: ["3273", "3274"],
    331115: ["3311", "3312"], 331315: ["3313", "3314"], 331500: ["3315"],
    332110: ["3321"], 332215: ["3322", "3325", "3326", "3327"], 332300: ["3323"], 332400: ["3324"],
    332810: ["3328"], 332900: ["3329"],
    333100: ["3331"], 333200: ["3332"], 333310: ["3333"], 333410: ["3334"], 333510: ["3335"],
    333610: ["3336"], 333900: ["3339"],
    334110: ["3341"], 334200: ["3342"], 334315: ["3343", "3346"], 334410: ["3344"], 334500: ["3345"],
    335105: ["3351", "3352"], 335310: ["3353"], 335900: ["3359"],
    336105: ["3361", "3362", "3363"], 336410: ["3364"], 336610: ["3366"], 336995: ["3365", "3369"],
    337: ["337"], 339110: ["3391"], 339900: ["3399"],
}

# Runs: (label, IRS tax year file, Census concentration year). The first is the primary pairing.
RUNS = [("2012", "irs_sourcebook_2012/2012sb1.csv", 2012),
        ("2013", "irs_sourcebook_2013/2013sb1.csv", 2012),
        ("2007", "irs_sourcebook_2007/07sb1.csv", 2007)]
CENSUS_FILES = {2012: ("EC1231SR2.dat", "NAICS2012", "NAICS2012_TTL"),
                2007: ("EC0731SR12.dat", "NAICS2007", "NAICS2007_MEANING")}

# Demsetz's published numbers, typed from the paper (pp. 6-9) so the comparison table is reproducible.
PAPER_T1 = [("10-20%", 14, 6.7, 9.0, 10.8, 10.3, 9.2), ("20-30%", 22, 4.5, 9.1, 9.7, 10.4, 8.4),
            ("30-40%", 24, 5.2, 8.7, 9.9, 11.0, 8.7), ("40-50%", 21, 5.8, 9.0, 9.5, 9.0, 8.3),
            ("50-60%", 11, 6.7, 9.8, 10.5, 13.4, 10.1), ("over 60%", 3, 5.3, 10.1, 11.5, 23.1, 12.5)]
PAPER_T2 = [("10-20%", 14, 7.3, 9.5, 10.6, 8.0, 8.8), ("20-30%", 22, 4.4, 8.6, 9.9, 10.6, 8.4),
            ("30-40%", 24, 5.1, 9.0, 9.4, 11.7, 8.8), ("40-50%", 21, 4.8, 9.5, 11.2, 9.4, 8.7),
            ("50-60%", 11, 0.9, 9.6, 10.8, 12.2, 8.4), ("over 60%", 3, 5.0, 8.6, 10.3, 21.6, 11.3)]
PAPER_T3 = [("R4-R1", -1.4, 0.21, 0.07, 0.09), ("R4-R2", -2.6, 0.12, 0.06, 0.04),
            ("R4-R3", -3.1, 0.10, 0.05, 0.04)]


def size_schemes():
    """Map IRS asset classes to Demsetz's four size classes, in 1963 dollars and in today's dollars."""
    cpi = pd.read_csv(RAW / "cpi_u_monthly.csv", parse_dates=["observation_date"])
    cpi = cpi.groupby(cpi.observation_date.dt.year).CPIAUCNS.mean()
    factor = cpi[2012] / cpi[1963]
    edges = sorted(set(IRS_AC_LOWER.values()) - {1})
    real = [min(edges, key=lambda e: abs(np.log(e / (x * factor)))) for x in DEMSETZ_EDGES_1963]
    schemes = {"real": real, "nominal": DEMSETZ_EDGES_1963}
    rows = []
    for name, cut in schemes.items():
        for k, (lo, hi) in enumerate(zip([0] + cut, cut + [np.inf]), start=1):
            rows.append(dict(scheme=name, size_class=f"R{k}", lower_thousands=lo, upper_thousands=hi,
                             cpi_1963=round(cpi[1963], 2), cpi_2012=round(cpi[2012], 2),
                             factor=round(factor, 2)))
    print(f"CPI-U 1963 = {cpi[1963]:.2f}, 2012 = {cpi[2012]:.2f}, factor {factor:.2f}; "
          f"Demsetz edges {DEMSETZ_EDGES_1963} become {real} (thousands)")
    return schemes, pd.DataFrame(rows)


def assign(ac, cut):
    lower = IRS_AC_LOWER[ac]
    return 1 + sum(lower >= c for c in cut)


def load_irs(path, schemes):
    """Size-class profit, interest and assets for each manufacturing industry, plus suppression flags."""
    x = pd.read_csv(RAW / path)
    x.columns = [c.strip().upper() for c in x.columns]
    x = x[(x.TAB_NUM == 1) & x.INDY_CD.isin(list(IRS_TO_NAICS))]
    n_ind = x.INDY_CD.nunique()
    x = x[x.AC >= 3].copy()  # AC 1 is the industry total, AC 2 the returns reporting zero assets
    for c in ["WT_CT", "TOT_ASSTS", "NET_INCM", "INTRST_PD", "COMP_TX_AFTR_CRS"]:
        x[c] = pd.to_numeric(x[c], errors="coerce").fillna(0.0)
    x["num"] = x.NET_INCM + x.INTRST_PD
    x["num_at"] = x.NET_INCM - x.COMP_TX_AFTR_CRS + x.INTRST_PD
    print(f"  {path}: {n_ind} manufacturing industries, {len(x)} industry-by-asset-class cells")
    out = {}
    for name, cut in schemes.items():
        x["g"] = x.AC.map(lambda a: assign(a, cut))
        g = x.groupby(["INDY_CD", "g"])[["WT_CT", "TOT_ASSTS", "num", "num_at"]].sum().unstack("g")
        wide = pd.DataFrame(index=g.index)
        for k in range(1, 5):
            wide[f"firms{k}"] = g["WT_CT"].get(k, 0)
            wide[f"assets{k}"] = g["TOT_ASSTS"].get(k, 0)
            wide[f"R{k}"] = 100 * g["num"].get(k, np.nan) / wide[f"assets{k}"].replace(0, np.nan)
            wide[f"R{k}_at"] = 100 * g["num_at"].get(k, np.nan) / wide[f"assets{k}"].replace(0, np.nan)
            wide[f"num{k}"] = g["num"].get(k, 0)
        # A cell flagged 2 was folded into the next lower IRS class; it crosses a Demsetz boundary when
        # it is the lowest IRS class of its group. Flag 3 cells were deleted and survive only in totals.
        low_edges = {ac for ac, lo in IRS_AC_LOWER.items() if lo in cut}
        crossed = x[(x.TOT_ASSTS_IND == 2) & x.AC.isin(low_edges)].groupby("INDY_CD").size()
        deleted = x[x.TOT_ASSTS_IND == 3].groupby("INDY_CD").size()
        # Deleted cells that sit in the smallest or largest class leave R1 or R4 built from part of the class.
        del_end = x[(x.TOT_ASSTS_IND == 3) & x.g.isin([1, 4])].groupby("INDY_CD").size()
        wide["flag_crossed"] = crossed.reindex(wide.index).fillna(0).astype(int)
        wide["flag_deleted"] = deleted.reindex(wide.index).fillna(0).astype(int)
        wide["flag_deleted_r1_r4"] = del_end.reindex(wide.index).fillna(0).astype(int)
        out[name] = wide
    return out


def load_census(year):
    """Published CR4 and shipments for every manufacturing NAICS code (3 to 6 digits)."""
    fname, code, title = CENSUS_FILES[year]
    c = pd.read_csv(RAW / "census" / fname, sep="|", dtype=str)
    c.columns = [col.strip() for col in c.columns]
    c[code] = c[code].str.strip()
    allc = c[c.CONCENFI == "004"].set_index(code)
    top4 = c[c.CONCENFI == "856"].set_index(code)
    d = pd.DataFrame({"label": allc[title], "shipments": pd.to_numeric(allc.RCPTOT, errors="coerce"),
                      "cr4": pd.to_numeric(top4.CCORCPPCT, errors="coerce")})
    d.loc[d.cr4 <= 0, "cr4"] = np.nan  # 0 with a flag means withheld
    print(f"  Census {year}: {len(d)} NAICS codes, {d.cr4.notna().sum()} with a published CR4")
    return d


def industry_cr4(census, prefixes):
    """CR4 at the level the IRS industry is defined, and a 6-digit shipment-weighted alternative."""
    own = census.loc[census.index.isin(prefixes)].dropna(subset=["cr4", "shipments"])
    six = census[(census.index.str.len() == 6) & census.index.str.startswith(tuple(prefixes))]
    six = six.dropna(subset=["cr4", "shipments"])
    total = census.loc[census.index.isin(prefixes), "shipments"].sum()
    return pd.Series({
        "cr4": np.average(own.cr4, weights=own.shipments) if len(own) else np.nan,
        "cr4_6digit": np.average(six.cr4, weights=six.shipments) if len(six) else np.nan,
        "shipments_bn": total / 1e6,
        "coverage_6digit": six.shipments.sum() / total if total else np.nan,
    })


def irs_titles(path):
    doc = pd.read_excel(RAW / path, sheet_name="Industry code titles", header=None)
    t = {}
    for _, r in doc.iterrows():
        for col_code, col_name in [(2, 3), (1, 2)]:
            code = pd.to_numeric(r[col_code], errors="coerce")
            if pd.notna(code) and isinstance(r[col_name], str):
                t.setdefault(int(code), r[col_name].strip())
    return t


def build(label, irs_file, census_year, schemes, census_cache):
    print(f"\nRun {label}: IRS tax year {label} with the {census_year} Economic Census")
    irs = load_irs(irs_file, schemes)
    cen = census_cache[census_year]
    conc = pd.DataFrame({k: industry_cr4(cen, v) for k, v in IRS_TO_NAICS.items()}).T
    conc_07 = pd.DataFrame({k: industry_cr4(census_cache[2007], v) for k, v in IRS_TO_NAICS.items()}).T
    titles = irs_titles("irs_sourcebook_2013/13sbfltfiledocumentation.xls")
    frames = {}
    for name, wide in irs.items():
        d = wide.join(conc).join(conc_07[["cr4"]].rename(columns={"cr4": "cr4_2007"}))
        d["industry"] = [titles.get(i, str(i)) for i in d.index]
        d["d_cr4"] = d.cr4 - d.cr4_2007
        n0 = len(d)
        keep = d[[f"assets{k}" for k in range(1, 5)]].gt(0).all(axis=1) & d.cr4.notna()
        dropped = d.loc[~keep, "industry"].tolist()
        d = d[keep].copy()
        print(f"  [{name}] kept {len(d)} of {n0} industries; dropped (an empty size class or no CR4): "
              f"{dropped if dropped else 'none'}; {int((d.flag_crossed > 0).sum())} kept industries "
              f"have a suppressed cell folded across a size boundary; "
              f"{int((d.flag_deleted_r1_r4 > 0).sum())} have a deleted cell inside R1 or R4")
        d["cr_class"] = pd.cut(d.cr4, CR_BINS, labels=CR_LABELS, right=False)
        d["R"] = d[["R1", "R2", "R3", "R4"]].mean(axis=1)
        d.index.name = "irs_code"
        frames[name] = d
    return frames


def tables(d, label, scheme):
    rows = []
    for cls, g in d.groupby("cr_class", observed=True):
        r_u = [g[f"R{k}"].mean() for k in range(1, 5)]
        r_w = [100 * g[f"num{k}"].sum() / g[f"assets{k}"].sum() for k in range(1, 5)]
        for wname, r in [("unweighted", r_u), ("asset-weighted", r_w)]:
            rows.append(dict(year=label, scheme=scheme, weighting=wname, cr_class=cls, industries=len(g),
                             R1=r[0], R2=r[1], R3=r[2], R4=r[3], R=np.mean(r)))
    return rows


def ols(y, X, data):
    Xc = sm.add_constant(data[X])
    classic = sm.OLS(data[y], Xc).fit()
    robust = sm.OLS(data[y], Xc).fit(cov_type="HC1")
    return classic, robust


def regressions(d, label, scheme, with_change=True):
    rows = []
    d = d.copy()
    for k in (1, 2, 3):
        d[f"g4{k}"] = d.R4 - d[f"R{k}"]
    specs = [(f"R4-R{k}", f"g4{k}", ["cr4"]) for k in (1, 2, 3)]
    specs += [("R1", "R1", ["cr4"]), ("R4", "R4", ["cr4"]), ("R4-R1 (after tax)", "g_at", ["cr4"]),
              ("R4-R1 (6-digit CR4)", "g41", ["cr4_6digit"])]
    if with_change:
        specs += [(f"R4-R{k} with change", f"g4{k}", ["cr4", "d_cr4"]) for k in (1, 2, 3)]
    d["g_at"] = d.R4_at - d.R1_at
    for name, y, X in specs:
        sub = d.dropna(subset=[y] + X)
        c, r = ols(y, X, sub)
        for x in X:
            rows.append(dict(year=label, scheme=scheme, dependent=name, regressor=x, n=int(c.nobs),
                             intercept=c.params["const"], coef=c.params[x], se=c.bse[x], p=c.pvalues[x],
                             se_hc1=r.bse[x], p_hc1=r.pvalues[x], r2=c.rsquared))
    return rows


def pooled_regressions(p):
    """Stack 2007, 2012 and 2013: year fixed effects, standard errors clustered by industry."""
    rows = []
    for k in (1, 2, 3):
        p[f"g4{k}"] = p.R4 - p[f"R{k}"]
    years = pd.get_dummies(p.year, prefix="y", drop_first=True).astype(float)
    for name, y in [("R4-R1", "g41"), ("R4-R2", "g42"), ("R4-R3", "g43"), ("R1", "R1"), ("R4", "R4")]:
        X = sm.add_constant(pd.concat([p[["cr4"]], years], axis=1))
        f = sm.OLS(p[y], X).fit(cov_type="cluster", cov_kwds={"groups": p.irs_code})
        rows.append(dict(year="pooled 2007+2012+2013", scheme="real", dependent=name, regressor="cr4",
                         n=int(f.nobs), intercept=f.params["const"], coef=f.params["cr4"],
                         se=f.bse["cr4"], p=f.pvalues["cr4"], se_hc1=np.nan, p_hc1=np.nan,
                         r2=f.rsquared))
    print(f"  pooled: {len(p)} industry-years, {p.irs_code.nunique()} industries")
    return rows


def manufacturing_context(cut):
    """All manufacturing, 2012: officers' pay and the S-corporation share of assets by size class."""
    t1 = pd.read_csv(RAW / "irs_sourcebook_2012/2012sb1.csv")
    t1.columns = [c.strip().upper() for c in t1.columns]
    t1 = t1[(t1.TAB_NUM == 1) & (t1.INDY_CD == 31) & (t1.AC >= 3)].copy()
    t1["g"] = t1.AC.map(lambda a: assign(a, cut))
    items = ["WT_CT", "TOT_ASSTS", "NET_INCM", "INTRST_PD", "CMPNSTN_OFFCRS", "INTNGBL_ASSTS",
             "ACCUM_AMORT", "OTHR_INVSMTS"]
    t1[items] = t1[items].apply(pd.to_numeric, errors="coerce").fillna(0.0)
    g = t1.groupby("g")[items].sum()
    # Form 1120S table (TAB_NUM 3) uses finer small classes: AC 3-7 are under $5M, 8-10 are $5-50M,
    # 11-12 are $50M and up, so S-corporation assets can be split only at $5M and $50M.
    t3 = pd.read_csv(RAW / "irs_sourcebook_2012/2012sb3.csv")
    t3.columns = [c.strip().upper() for c in t3.columns]
    t3 = t3[(t3.TAB_NUM == 3) & (t3.INDY_CD == 31) & (t3.AC >= 3)]
    s_assets = t3.groupby(pd.cut(t3.AC, [2, 7, 10, 12], labels=[1, 2, 3])).TOT_ASSTS.sum()
    out = pd.DataFrame({"size_class": [f"R{k}" for k in g.index], "returns": g.WT_CT.values,
                        "assets_bn": g.TOT_ASSTS.values / 1e6,
                        "return_pct": 100 * (g.NET_INCM + g.INTRST_PD).values / g.TOT_ASSTS.values,
                        "officer_pay_pct_assets": 100 * g.CMPNSTN_OFFCRS.values / g.TOT_ASSTS.values,
                        "intangibles_pct_assets": 100 * (g.INTNGBL_ASSTS - g.ACCUM_AMORT).values
                        / g.TOT_ASSTS.values,
                        "other_investments_pct_assets": 100 * g.OTHR_INVSMTS.values / g.TOT_ASSTS.values})
    s_share = [s_assets.get(1), s_assets.get(2), s_assets.get(3), np.nan]
    out["s_corp_share_assets_pct"] = [100 * s / a if s is not None and s == s else np.nan
                                      for s, a in zip(s_share, out.assets_bn * 1e6)]
    out.loc[2, "s_corp_share_assets_pct"] = np.nan  # S-corporations of $50M+ cannot be split at $500M
    print("  manufacturing 2012 by size class:\n" + out.round(1).to_string(index=False))
    return out.round(4)


def paper_tables():
    rows = []
    for tname, tab in [("Table 1 unweighted", PAPER_T1), ("Table 2 asset-weighted", PAPER_T2)]:
        for cls, n, r1, r2, r3, r4, r in tab:
            rows.append(dict(table=tname, cr_class=cls, industries=n, R1=r1, R2=r2, R3=r3, R4=r4, R=r))
    for dep, a, b, se, r2 in PAPER_T3:
        rows.append(dict(table="Table 3", cr_class=dep, intercept=a, coef=b, se=se, r2=r2))
    return pd.DataFrame(rows)


def figures(tab, primary):
    paper = pd.DataFrame(PAPER_T1, columns=["cr_class", "n", "R1", "R2", "R3", "R4", "R"])
    mod = tab[(tab.year == "2012") & (tab.scheme == "real") & (tab.weighting == "unweighted")]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.2), sharey=True)
    for ax, df, title in [(axes[0], paper, "1963 (Demsetz, Table 1)"), (axes[1], mod, "2012 (IRS Source Book)")]:
        xs = np.arange(len(df))
        ax.plot(xs, df.R1, "o-", color="#b45f06", label="Smallest firms (R1)")
        ax.plot(xs, df.R4, "s-", color="#1f4e79", label="Largest firms (R4)")
        ax.set_xticks(xs, df.cr_class, rotation=30)
        ax.set_title(title)
        ax.set_xlabel("Four-firm concentration ratio")
        ax.grid(alpha=0.3)
    axes[0].set_ylabel("(Profit + interest) / total assets, %")
    axes[0].legend(frameon=False)
    fig.tight_layout()
    fig.savefig(OUT / "size_returns_by_concentration.png", dpi=150)
    plt.close(fig)

    d = primary
    fig, ax = plt.subplots(figsize=(7, 4.6))
    gap = d.R4 - d.R1
    ax.scatter(d.cr4, gap, color="#1f4e79", alpha=0.75)
    b = np.polyfit(d.cr4, gap, 1)
    xs = np.linspace(d.cr4.min(), d.cr4.max(), 50)
    ax.plot(xs, b[1] + b[0] * xs, color="#1f4e79", label=f"2012 fit: slope {b[0]:.2f}")
    ax.plot(xs, -1.4 + 0.21 * xs, "--", color="#999999", label="Demsetz 1963 fit: slope 0.21")
    for i, r in d.assign(gap=gap).nlargest(4, "gap").iterrows():
        ax.annotate(r.industry[:28], (r.cr4, r.gap), fontsize=7, xytext=(4, 2), textcoords="offset points")
    ax.axhline(0, color="black", lw=0.6)
    ax.set_xlabel("Four-firm concentration ratio, 2012 (%)")
    ax.set_ylabel("R4 minus R1, percentage points")
    ax.set_title("Large-firm advantage and concentration, 2012 manufacturing")
    ax.legend(frameon=False, fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "gap_vs_concentration.png", dpi=150)
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    schemes, thresholds = size_schemes()
    thresholds.to_csv(OUT / "size_thresholds.csv", index=False)
    census = {y: load_census(y) for y in CENSUS_FILES}
    tab_rows, reg_rows, pooled, primary = [], [], [], None
    for label, irs_file, cyear in RUNS:
        frames = build(label, irs_file, cyear, schemes, census)
        for scheme, d in frames.items():
            cols = ["industry", "cr4", "cr4_6digit", "cr4_2007", "d_cr4", "cr_class", "shipments_bn",
                    "coverage_6digit", "R1", "R2", "R3", "R4", "R", "R1_at", "R4_at",
                    "firms1", "firms2", "firms3", "firms4", "assets1", "assets2", "assets3", "assets4",
                    "num1", "num2", "num3", "num4",
                    "flag_crossed", "flag_deleted", "flag_deleted_r1_r4"]
            if scheme == "real":
                d[cols].round(4).to_csv(OUT / f"industries_{label}.csv")
            else:
                d[cols].round(4).to_csv(OUT / f"industries_{label}_nominal.csv")
            tab_rows += tables(d, label, scheme)
            reg_rows += regressions(d, label, scheme, with_change=cyear != 2007)
            if scheme == "real":
                pooled.append(d.assign(year=label))
            if label == "2012" and scheme == "real":
                reg_rows += regressions(d[d.flag_crossed == 0], "2012 no folded cells", scheme)
                reg_rows += regressions(d[d.flag_deleted_r1_r4 == 0], "2012 no deleted cells in R1 or R4",
                                        scheme)
                primary = d
    reg_rows += pooled_regressions(pd.concat(pooled).reset_index())
    manufacturing_context(schemes["real"]).to_csv(OUT / "manufacturing_size_classes.csv", index=False)
    tab = pd.DataFrame(tab_rows)
    reg = pd.DataFrame(reg_rows)
    tab.round(4).to_csv(OUT / "demsetz_tables.csv", index=False)
    reg.round(6).to_csv(OUT / "regressions.csv", index=False)
    paper_tables().to_csv(OUT / "paper_tables.csv", index=False)
    figures(tab, primary)

    show = tab[(tab.year == "2012") & (tab.scheme == "real")]
    print("\nTable 1 and 2, 2012, size classes in today's dollars:")
    print(show.round(1).to_string(index=False))
    key = reg[(reg.year == "2012") & (reg.scheme == "real") & (reg.regressor == "cr4")]
    print("\nTable 3, 2012:")
    print(key[["dependent", "n", "intercept", "coef", "se", "p", "se_hc1", "p_hc1", "r2"]].round(3).to_string(index=False))


if __name__ == "__main__":
    main()
