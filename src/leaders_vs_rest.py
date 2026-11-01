"""Extension: Demsetz's large-firm advantage in 2017 and 2022, in the Economic Census itself.

The IRS stopped publishing profits by industry and asset size after tax year 2013, so this script
asks Demsetz's question with the newest data that splits every industry into its leaders and everyone
else. The 2017 and 2022 Economic Census concentration tables report revenue, annual payroll and
employment for the four largest firms and for all firms in each 6-digit NAICS industry, in every
sector the census covers. From those I compute, for the top four and for the rest of the industry:

    payroll share   = annual payroll / revenue       (cents of each sales dollar paid to workers)
    revenue/worker  = revenue / employees           (a crude labor-productivity measure)

Demsetz's efficiency account, and the "superstar firm" account built on it (Autor, Dorn, Katz,
Patterson and Van Reenen 2020), predict that leaders spend a smaller share of revenue on payroll
than their rivals, and that the gap is wider where the top four hold more of the market and widens
where concentration rises.

Usage, from the repository root:
    python src/leaders_vs_rest.py
Writes results/leaders_<year>.csv, results/leaders_changes.csv, results/leaders_regressions.csv,
results/leaders_names.csv and results/leaders_gap_by_cr4.png.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw" / "census"
OUT = ROOT / "results"

FILES = {2017: ("EC1700SIZECONCEN.dat", "NAICS2017", "NAICS2017_TTL"),
         2022: ("EC2200SIZECONCEN.dat", "NAICS2022", "NAICS2022_LABEL")}
# Finance and insurance (52) is excluded: its census "revenue" includes premiums and interest, so
# payroll per dollar of revenue does not measure the same thing as in other sectors.
EXCLUDED_SECTORS = {"52"}
MIN_FIRMS = 8  # at least four firms outside the top four, so "the rest" is more than one or two firms
CR_BINS = [0, 20, 40, 60, 101]
CR_LABELS = ["under 20%", "20-40%", "40-60%", "60% and over"]
SECTOR_NAMES = {"21": "Mining", "22": "Utilities", "23": "Construction", "31": "Manufacturing",
                "42": "Wholesale", "44": "Retail", "48": "Transportation", "51": "Information",
                "53": "Real estate", "54": "Professional services", "56": "Administrative services",
                "61": "Education", "62": "Health care", "71": "Arts and recreation",
                "72": "Hotels and restaurants", "81": "Other services"}


def load(year):
    fname, code, title = FILES[year]
    c = pd.read_csv(RAW / fname, sep="|", dtype=str)
    c.columns = [col.lstrip("#").strip() for col in c.columns]
    c = c[c[code].str.len() == 6]
    keep_cols = ["FIRM", "RCPTOT", "PAYANN", "EMP"]
    parts = {}
    for cid, name in [("001", "all"), ("604", "top4")]:
        p = c[c.CONCENFI == cid].set_index(code)
        withheld = p[[f"{k}_F" for k in keep_cols]].fillna("").apply(lambda s: s.str.strip() != "").any(axis=1)
        vals = p[keep_cols].apply(pd.to_numeric, errors="coerce")
        vals[withheld] = np.nan
        parts[name] = vals.add_suffix(f"_{name}")
    d = parts["all"].join(parts["top4"], how="inner")
    d["industry"] = c[c.CONCENFI == "001"].set_index(code)[title]
    d["sector"] = d.index.str[:2].map(lambda s: "31" if s in ("31", "32", "33") else
                                      "44" if s in ("44", "45") else "48" if s in ("48", "49") else s)
    d["cr4"] = 100 * d.RCPTOT_top4 / d.RCPTOT_all
    # Top four's share of employment: a concentration measure with no revenue in it, used to check
    # that the revenue-based results are not a by-product of revenue sitting on both sides.
    d["emp_share4"] = 100 * d.EMP_top4 / d.EMP_all
    n0 = len(d)
    d = d[~d.sector.isin(EXCLUDED_SECTORS)]
    n1 = len(d)
    d = d.dropna(subset=["RCPTOT_all", "RCPTOT_top4", "PAYANN_all", "PAYANN_top4", "EMP_all", "EMP_top4"])
    n2 = len(d)
    d = d[d.FIRM_all >= MIN_FIRMS]
    for k in ["RCPTOT", "PAYANN", "EMP"]:
        d[f"{k}_rest"] = d[f"{k}_all"] - d[f"{k}_top4"]
    d = d[(d.RCPTOT_rest > 0) & (d.EMP_rest > 0) & (d.PAYANN_rest > 0) & (d.EMP_top4 > 0)].copy()
    print(f"{year}: {n0} industries; {n0 - n1} in finance dropped; {n1 - n2} with a withheld or "
          f"flagged value dropped; {n2 - len(d)} with fewer than {MIN_FIRMS} firms or an empty "
          f"remainder dropped; {len(d)} kept")
    for g in ["top4", "rest"]:
        d[f"pay_share_{g}"] = 100 * d[f"PAYANN_{g}"] / d[f"RCPTOT_{g}"]
        d[f"rev_per_worker_{g}"] = d[f"RCPTOT_{g}"] / d[f"EMP_{g}"]  # $ thousands per employee
        d[f"wage_{g}"] = d[f"PAYANN_{g}"] / d[f"EMP_{g}"]
    d["pay_gap"] = d.pay_share_rest - d.pay_share_top4
    d["log_productivity_ratio"] = np.log(d.rev_per_worker_top4 / d.rev_per_worker_rest)
    d["log_wage_ratio"] = np.log(d.wage_top4 / d.wage_rest)
    d["leader_lower_pay_share"] = d.pay_gap > 0
    d["cr_class"] = pd.cut(d.cr4, CR_BINS, labels=CR_LABELS, right=False)
    d["revenue_bn"] = d.RCPTOT_all / 1e6
    d.index.name = "naics"
    return d


def fit(formula, data, weights=None):
    m = smf.wls(formula, data=data, weights=weights) if weights is not None else smf.ols(formula, data=data)
    return m.fit(cov_type="HC1")


def regressions(levels, changes):
    rows = []
    for year, d in levels.items():
        for y in ["pay_gap", "log_productivity_ratio", "log_wage_ratio"]:
            for label, sub, fe in [("all sectors", d, " + C(sector)"), ("manufacturing", d[d.sector == "31"], "")]:
                for wname, w in [("equal", None), ("revenue", sub.RCPTOT_all)]:
                    f = fit(f"{y} ~ cr4{fe}", sub, w)
                    rows.append(dict(test=f"levels {year}", sample=label, weights=wname, dependent=y,
                                     regressor="cr4", n=int(f.nobs), coef=f.params["cr4"], se=f.bse["cr4"],
                                     p=f.pvalues["cr4"], r2=f.rsquared))
        f = fit("pay_gap ~ emp_share4 + C(sector)", d)
        rows.append(dict(test=f"levels {year}", sample="all sectors", weights="equal", dependent="pay_gap",
                         regressor="emp_share4", n=int(f.nobs), coef=f.params["emp_share4"],
                         se=f.bse["emp_share4"], p=f.pvalues["emp_share4"], r2=f.rsquared))
    for x in ["d_cr4", "d_emp_share4"]:
        for y in ["d_pay_gap", "d_log_productivity_ratio", "d_log_wage_ratio"]:
            for label, sub, fe in [("all sectors", changes, " + C(sector)"),
                                   ("manufacturing", changes[changes.sector == "31"], "")]:
                for wname, w in [("equal", None), ("revenue", sub.revenue_bn)]:
                    f = fit(f"{y} ~ {x}{fe}", sub, w)
                    rows.append(dict(test="changes 2017-2022", sample=label, weights=wname, dependent=y,
                                     regressor=x, n=int(f.nobs), coef=f.params[x], se=f.bse[x],
                                     p=f.pvalues[x], r2=f.rsquared))
    return pd.DataFrame(rows)


def by_class(d, year):
    rows = []
    for cls, g in d.groupby("cr_class", observed=True):
        rows.append(dict(year=year, cr_class=cls, industries=len(g), revenue_bn=g.revenue_bn.sum(),
                         pay_share_top4_median=g.pay_share_top4.median(),
                         pay_share_rest_median=g.pay_share_rest.median(),
                         pay_gap_median=g.pay_gap.median(),
                         pct_leaders_lower=100 * g.leader_lower_pay_share.mean(),
                         productivity_ratio_median=np.exp(g.log_productivity_ratio.median()),
                         wage_ratio_median=np.exp(g.log_wage_ratio.median())))
    rows.append(dict(year=year, cr_class="all", industries=len(d), revenue_bn=d.revenue_bn.sum(),
                     pay_share_top4_median=d.pay_share_top4.median(),
                     pay_share_rest_median=d.pay_share_rest.median(), pay_gap_median=d.pay_gap.median(),
                     pct_leaders_lower=100 * d.leader_lower_pay_share.mean(),
                     productivity_ratio_median=np.exp(d.log_productivity_ratio.median()),
                     wage_ratio_median=np.exp(d.log_wage_ratio.median())))
    return rows


def figure(d):
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    colors = np.where(d.sector == "31", "#1f4e79", "#b45f06")
    ax.scatter(d.cr4, d.pay_gap.clip(-30, 30), s=10, c=colors, alpha=0.45)
    bins = pd.cut(d.cr4, range(0, 101, 10))
    med = d.groupby(bins, observed=True).pay_gap.median()
    ax.plot([b.mid for b in med.index], med.values, "k-o", lw=2, ms=4, label="Median by 10-point band")
    ax.axhline(0, color="black", lw=0.6)
    ax.scatter([], [], c="#1f4e79", s=10, label="Manufacturing")
    ax.scatter([], [], c="#b45f06", s=10, label="Other sectors")
    ax.set_xlabel("Top four firms' share of industry revenue, 2022 (%)")
    ax.set_ylabel("Rest's payroll share minus top four's (points)")
    ax.set_title("Top four firms vs. the rest of their industry, 2022")
    ax.legend(frameon=False, fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT / "leaders_gap_by_cr4.png", dpi=150)
    plt.close(fig)


def main():
    OUT.mkdir(exist_ok=True)
    levels = {y: load(y) for y in FILES}
    cols = ["industry", "sector", "cr4", "emp_share4", "cr_class", "revenue_bn", "FIRM_all", "pay_share_top4",
            "pay_share_rest", "pay_gap", "rev_per_worker_top4", "rev_per_worker_rest", "wage_top4",
            "wage_rest", "log_productivity_ratio", "log_wage_ratio", "RCPTOT_top4", "PAYANN_top4",
            "EMP_top4", "RCPTOT_rest", "PAYANN_rest", "EMP_rest"]
    for y, d in levels.items():
        d[cols].round(4).to_csv(OUT / f"leaders_{y}.csv")
    a, b = levels[2017], levels[2022]
    measures = ["cr4", "emp_share4", "pay_gap", "log_productivity_ratio", "log_wage_ratio"]
    ch = a[measures + ["sector"]].join(b[["industry", "revenue_bn"] + measures],
                                       how="inner", suffixes=("_17", "_22"))
    for m in measures:
        ch[f"d_{m}"] = ch[f"{m}_22"] - ch[f"{m}_17"]
    print(f"changes: {len(ch)} industries with the same 6-digit code kept in both years")
    ch.round(4).to_csv(OUT / "leaders_changes.csv")

    reg = regressions(levels, ch)
    reg.round(6).to_csv(OUT / "leaders_regressions.csv", index=False)
    summary = pd.DataFrame(by_class(a, 2017) + by_class(b, 2022))
    summary.round(4).to_csv(OUT / "leaders_by_cr4.csv", index=False)

    big = b[b.cr4 >= 50].nlargest(12, "revenue_bn")
    names = big[["industry", "sector", "cr4", "revenue_bn", "pay_share_top4", "pay_share_rest",
                 "rev_per_worker_top4", "rev_per_worker_rest", "wage_top4", "wage_rest"]].copy()
    names["sector"] = names.sector.map(SECTOR_NAMES)
    names.round(4).to_csv(OUT / "leaders_names.csv")
    figure(b)

    print("\nMedians by concentration class:")
    print(summary.round(2).to_string(index=False))
    print("\nRegressions (HC1 standard errors):")
    print(reg[reg.weights == "equal"].round(4).to_string(index=False))
    print("\nLargest industries with CR4 of 50% or more, 2022:")
    print(names.round(1).to_string())


if __name__ == "__main__":
    main()
