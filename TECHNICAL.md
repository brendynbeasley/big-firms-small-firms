# Technical notes

The technical companion to the [README](README.md). Every number below is produced by the two scripts in `src/`
into `results/`. The full tables are in [results/FINDINGS.md](results/FINDINGS.md).

## The original study

Harold Demsetz, "Industry Structure, Market Rivalry, and Public Policy," *Journal of Law and Economics* 16(1),
April 1973, pp. 1–9. Using 1963 IRS returns for 95 three-digit manufacturing industries, split into four asset-size
classes (under $0.5M, $0.5–5M, $5–50M, over $50M), Demsetz computed (profit + interest) / total assets by class and
grouped industries by the 1963 four-firm concentration ratio. In the three industries above 60%, the largest class
earned 23.1% and the smallest 5.3% (Table 1). Regressing the large-minus-small gap on concentration gave
R4 − R1 = −1.4 + 0.21 C63 (s.e. 0.07, r² = 0.09), with smaller slopes against R2 (0.12) and R3 (0.10) (Table 3).
Small firms' returns showed no rise with concentration, which he read as evidence against collusion.

## Headline results

| | Industries | Slope of R4 − R1 on CR4 | s.e. | p | Slope of R1 on CR4 | p |
|---|---|---|---|---|---|---|
| Demsetz, 1963 | 95 | 0.21 | 0.07 | < 0.01 | not reported | |
| Tax year 2012, 2012 Census (main run) | 58 | 0.250 | 0.097 | 0.012 | −0.223 | 0.020 |
| Tax year 2013, 2012 Census | 58 | 0.129 | 0.105 | 0.22 | −0.079 | 0.43 |
| Tax year 2007, 2007 Census | 60 | 0.093 | 0.103 | 0.37 | −0.036 | 0.72 |
| Pooled, year effects, clustered by industry | 176 | 0.158 | 0.078 | 0.043 | −0.113 | 0.12 |

In 2012 the largest class averaged 4.7% to 7.1% in every concentration band, against Demsetz's 23.1% at the top. The gap
widens with concentration because small-firm returns fall, not because large-firm returns rise.

## Data

All files are committed in `data/raw/` and were downloaded on 2026-11-01.

- **IRS Statistics of Income, Corporation Source Book flat files** (irs.gov/pub/irs-soi/12sbfltfile.zip,
  13sbfltfile.zip, 07sbflatfile.zip). Used: `2012sb1.csv`, `2013sb1.csv`, `07sb1.csv` (Table 1, all returns,
  13 asset classes by minor industry), `2012sb3.csv` (Form 1120S returns, for the S-corporation share) and the
  documentation workbooks. Money amounts are in thousands of dollars. The IRS discontinued the Source Book after tax
  year 2013.
- **Census Bureau, Economic Census concentration tables** (www2.census.gov/programs-surveys/economic-census/data/).
  `EC1231SR2.dat` (2012 manufacturing CR4 and shipments, 3- to 6-digit NAICS), `EC0731SR12.dat` (2007 manufacturing),
  `EC1700SIZECONCEN.dat` and `EC2200SIZECONCEN.dat` (2017 and 2022, all covered sectors, revenue, payroll and
  employment for the 4, 8, 20 and 50 largest firms and for all firms).
- **CPI-U, not seasonally adjusted** (FRED series CPIAUCNS, fred.stlouisfed.org/graph/fredgraph.csv?id=CPIAUCNS),
  `cpi_u_monthly.csv`.

## Method

Rules fixed before results were seen:

- **Size classes.** Demsetz's edges ($0.5M, $5M, $50M) are multiplied by CPI-U 2012 / 1963 = 229.59 / 30.62 = 7.50 and
  moved to the nearest IRS class boundary in log distance, giving $5M, $50M and $500M. Demsetz's nominal edges are run
  as a check. Returns reporting zero assets are excluded.
- **Return.** R = (net income less deficit + interest paid) / total assets, summed within the size class. An after-tax
  version subtracts total income tax after credits.
- **Concentration.** CR4 published for the NAICS code an IRS industry covers, shipment-weighted when the IRS industry
  spans several codes (for example 3111 and 3112 for animal food and grain milling). A shipment-weighted average of
  6-digit CR4s is the check.
- **Sample.** IRS manufacturing minor industries with positive assets in all four classes and a CR4. 58 of 64 survive in
  2012.
- **Concentration bands.** Demsetz's 10-point bands, with "under 10%" added.
- **Extension.** 6-digit industries with revenue, payroll and employment published (no withheld or range flag) for both
  the top four and all firms, at least 8 firms, finance and insurance excluded.

For industry $`j`$, size class $`k`$, and year $`t`$,

```math
R_{kjt} = \frac{\Pi_{kjt} + I_{kjt}}{A_{kjt}}, \qquad R_{4jt} - R_{kjt} = \alpha_k + \beta_k\,\text{CR4}_{jt} + \lambda_t + \varepsilon_{kjt}
```

Single-year regressions report conventional and HC1 standard errors. The pooled regression includes year effects
$`\lambda_t`$ and clusters by industry. Demsetz's Table 4 is replicated by adding $`\Delta\text{CR4}_j`$ from 2007 to 2012.

In the extension, for group $`g \in \{\text{top 4}, \text{rest}\}`$ of industry $`j`$ in sector $`s`$,

```math
s_{gj} = \frac{W_{gj}}{Y_{gj}}, \qquad \text{gap}_j = s_{\text{rest},j} - s_{\text{top 4},j} = a + b\,\text{CR4}_j + \mu_s + e_j
```

with HC1 errors, plus the log ratio of revenue per worker and of pay per worker.

One check was added after seeing results. The 2017 to 2022 change regression gave a large positive slope, and because
revenue enters both the concentration ratio and the payroll share, I reran it with the top four's employment share as
the concentration measure. The sign reversed, so the change result is treated as uninformative. A second check
was added on review: the IRS deletes some cells to protect disclosure, and in seven of the 58 industries of 2012
such a cell sits inside the smallest or largest class, so the regression is rerun without them.

## Full test statistics

**Demsetz's Table 3, size classes in 2012 dollars** (conventional s.e.; robust p in brackets):

| Run | R4 − R1 | R4 − R2 | R4 − R3 | R1 | R4 |
|---|---|---|---|---|---|
| 2012 | 0.250 (0.097) [0.080] | 0.043 (0.042) [0.27] | 0.008 (0.025) [0.82] | −0.223 (0.093) [0.088] | 0.027 (0.020) [0.19] |
| 2013 | 0.129 (0.105) [0.21] | 0.111 (0.052) [0.033] | 0.097 (0.034) [0.007] | −0.079 (0.100) [0.45] | 0.051 (0.027) [0.087] |
| 2007 | 0.093 (0.103) [0.25] | 0.119 (0.049) [0.010] | 0.060 (0.032) [0.083] | −0.036 (0.101) [0.67] | 0.057 (0.027) [0.021] |
| Pooled | 0.158 (0.078) | 0.091 (0.037) | 0.052 (0.029) | −0.113 (0.072) | 0.045 (0.018) |

Other checks for 2012: after-tax R4 − R1 slope 0.239 (p = 0.016); 6-digit CR4 0.286 (p = 0.010); dropping the one
industry with a withheld cell folded across a size boundary 0.251 (p = 0.012); dropping the seven industries
where a cell deleted for disclosure sits inside R1 or R4, so that class is only partly observed, 0.276 (s.e. 0.103,
p = 0.010, robust p = 0.082, N = 51). With Demsetz's nominal edges, the R1
class (under $500,000 of assets) has tiny denominators and the R4 − R1 slope is 2.36 with s.e. 3.56. Adding
ΔCR4 (2007 to 2012) to the 2012 regressions gives −0.096 (0.272), −0.135 (0.117) and −0.134 (0.069), against
Demsetz's +0.21, +0.37 and +0.29. In the 2013 run the R4 − R1 change coefficient is −0.537 (0.251), p = 0.037,
significant and of the opposite sign to his.

**Extension, 2022 levels, sector effects** (HC1): payroll gap on CR4 0.014 (0.016), p = 0.38, N = 770; log
revenue-per-worker ratio 0.0022 (0.0009), p = 0.014; log pay-per-worker ratio −0.0006 (0.0004), p = 0.14.
Payroll gap on the employment share −0.072 (0.021). **Changes 2017 to 2022**, N = 696: Δgap on ΔCR4 0.221 (0.040);
on Δ employment share −0.247 (0.055).

## Reproducing the results

```bash
pip install -r requirements.txt
rm -rf results
python src/demsetz_tables.py
python src/leaders_vs_rest.py
```

Both scripts run offline from `data/raw/` in under a minute and print rows loaded, kept and dropped.

## Repository layout

| Path | What it is |
|---|---|
| `src/demsetz_tables.py` | Demsetz's Tables 1 to 4 on IRS and Census data, checks, two figures |
| `src/leaders_vs_rest.py` | Extension on the 2017 and 2022 Census, one figure |
| `results/industries_<year>.csv` | Industry-level returns by size class and concentration |
| `results/demsetz_tables.csv`, `results/regressions.csv` | Tables 1 to 4 for every run |
| `results/leaders_*.csv` | Extension tables |

## References

- Autor, D., Dorn, D., Katz, L. F., Patterson, C. & Van Reenen, J. (2020). The fall of the labor share and the rise of
  superstar firms. *QJE* 135(2), 645–709.
- Bain, J. S. (1951). Relation of profit rate to industry concentration. *QJE* 65(3).
- Berry, S., Gaynor, M. & Scott Morton, F. (2019). Do increasing markups matter? Lessons from empirical industrial
  organization. *JEP* 33(3), 44–68.
- Demsetz, H. (1973). Industry structure, market rivalry, and public policy. *JLE* 16(1), 1–9.
- Schmalensee, R. (1989). Inter-industry studies of structure and performance. *Handbook of IO*, Vol. 2.
