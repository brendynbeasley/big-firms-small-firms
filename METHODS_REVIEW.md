# Methods review of Demsetz (1973)

- **Paper.** Harold Demsetz, "Industry Structure, Market Rivalry, and Public Policy," *Journal of Law and Economics*
  16(1), April 1973, pp. 1–9 (JSTOR stable URL jstor.org/stable/724822).
- **Statistical focus.** The size-class rates of return in Tables 1 and 2 (in particular the 23.1% return of the
  largest firms against 5.3% for the smallest in industries with a four-firm concentration ratio above 60%) and the
  Table 3 regression of the large-minus-small return gap on concentration (slope 0.21, standard error 0.07).
- **Review standard.** Current AEA Data and Code Availability Policy, and standard reporting of estimates,
  uncertainty, sample construction and variable definitions for an empirical paper.
- **What was read.** The full text of the published article (nine pages, including Tables 1 to 4 and footnotes 1 to
  6) in a JSTOR scan posted on a university course reading page. In that copy a few words at the right edge of pages
  2, 6 and 8 and parts of footnotes 4 and 6(3) are cut off, so statements about those passages are limited to what is
  legible. I did not examine the underlying 1963 IRS or Census volumes.

## Methods summary

### Research design

A single-year cross-section of industry aggregates. For each manufacturing industry, published IRS tabulations of
corporate returns by asset size provide profit, interest and assets for four size classes, and the industry's 1963
four-firm concentration ratio is attached. The design compares returns across size classes within industries and
relates the within-industry gap to concentration across industries. It is observational, with no source of exogenous
variation in concentration. The argument that identifies efficiency from collusion is theoretical (section III):
under collusion at a common price with common costs, rates of return should not vary with firm size, so a size gap
signals a cost or quality difference.

### Sampling strategy

The unit is a "three digit" industry from "internal revenue data" for 1963. The paper does not say how the 95
industries were selected from the IRS classification, how IRS industries were matched to Census concentration ratios
(which the Census published for four-digit SIC industries), or whether concentration ratios were aggregated, and if
so with what weights.

### Sample size

95 industries (the industry counts in Tables 1 and 2 sum to 95). The highest concentration band, "over 60%", contains
three industries, which are not named. The regressions in Tables 3 and 4 do not report the number of observations.

### Inclusion and exclusion criteria

Footnote 6(2) states that industries with no firms in the largest asset class (over $50 million) were dropped. That
rule removes industries made up only of small and medium firms, which are likely to be the least concentrated. As a
check, the author redefined the large and small groups industry by industry (the three largest and three smallest
populated asset categories) and reports the unweighted average difference RL − RS by concentration band, which rises
from 6.4 points (0–20%) to 14.0 points (over 60%). The number of industries in this check is not given.

### Independent and dependent variables

Dependent: R1 to R4, "accounting rates of return (profit plus interest)/total assets" for firms with assets under
$500,000, $500,000 to $5,000,000, $5,000,000 to $50,000,000 and over $50,000,000. Whether profit is before or after
income tax is not stated, nor which IRS line items were used. Independent: C63, the four-firm concentration ratio
"measured on industry sales". Table 4 adds C67 − C63, the change to 1967.

### Statistical methods

Tables 1 and 2 report averages of R1 to R4 within concentration bands, unweighted (each industry equal) and weighted
by assets. The column R is the simple average of the four size-class returns in each row, which can be confirmed from
the printed numbers (for the 10–20% row of Table 1, (6.7 + 9.0 + 10.8 + 10.3) / 4 = 9.2). Table 3 reports three
bivariate least-squares regressions of R4 − Rk on C63 with standard errors in parentheses and significance stars.
Table 4 adds C67 − C63. No other controls are used.

### Reported effect sizes

The Table 3 slopes (0.21, 0.12 and 0.10 percentage points of return gap per point of concentration) and the band
averages in Tables 1 and 2 are the effect sizes. The r² values are 0.09, 0.04 and 0.04.

### Confidence intervals

None are reported. From the reported standard error, an approximate 95% interval for the R4 − R1 slope is
0.21 ± 1.96 × 0.07, or about 0.07 to 0.35 (computed here, not in the paper).

### p-values, if applicable

Not reported as numbers. Stars mark the 1% and 5% levels. In the copy I read, the Table 3 legend is partly garbled,
and the Table 4 legend describes the stars as "confidence levels" where significance levels are meant.

### Missing data treatment

Not discussed beyond the exclusion of industries without large firms. The paper does not say whether any IRS cells
were withheld or combined for disclosure reasons, or how such cells were handled.

### Stated limitations

Footnote 4 notes that firms are classified by absolute size, so the "small" firms in some industries are relatively
large, and that comparing each industry's largest and smallest 10% of firms would be better. Footnote 5 notes that
large firms need not have a cost advantage at the margin. The text says the 1963 to 1967 span is too short to reveal
much variation in concentration, so the Table 4 change coefficients deserve little confidence. Footnote 6(1) reports a
check adding administrative salaries back to the smallest class's profits, which raised their return slightly and
produced no correlation with concentration.

## Statistics extraction table

| Statistic | Value and unit | Source location | What it measures | What it does not establish |
|---|---|---|---|---|
| Number of industries | 95 three-digit manufacturing industries | p. 5 text; Tables 1–2 counts | Sample size of the cross-section | How the industries were chosen or matched to concentration data |
| Size-class edges | $0.5M, $5M, $50M of total assets (1963 dollars) | p. 5 text | Boundaries of R1 to R4 | That the classes mean the same relative size in every industry (footnote 4) |
| R4, CR4 over 60% | 23.1% | Table 1, p. 6 | Unweighted mean return of the largest firms in 3 industries | Whether the result holds outside those 3 unnamed industries; any standard error |
| R1, CR4 over 60% | 5.3% | Table 1, p. 6 | Unweighted mean return of the smallest firms in the same 3 industries | That small firms in concentrated industries do not gain from collusion in general |
| R, CR4 over 60% vs 10–20% | 12.5% vs 9.2% | Table 1, p. 6 | Simple average of the four size-class returns | An industry-level return; R does not weight classes by their share of output |
| R4, asset-weighted, CR4 over 60% | 21.6% | Table 2, p. 6 | Asset-weighted return of the largest firms | Statistical significance of the difference from other bands |
| R1, asset-weighted, CR4 50–60% | 0.9% | Table 2, p. 6 | Asset-weighted return of the smallest firms in 11 industries | Why this cell is far below its neighbors (4.8% and 5.0%) |
| R4 − R1 on C63 | slope 0.21 (s.e. 0.07), intercept −1.4, r² = 0.09, 1% level | Table 3, p. 7 | Change in the large-small gap per point of concentration | Causality; that the gap reflects cost rather than accounting differences; N not reported |
| R4 − R2 on C63 | slope 0.12 (s.e. 0.06), intercept −2.6, r² = 0.04, 5% level | Table 3, p. 7 | Same, against the second class | Robustness to controls |
| R4 − R3 on C63 | slope 0.10 (s.e. 0.05), intercept −3.1, r² = 0.04, 5% level | Table 3, p. 7 | Same, against the third class | Robustness to controls |
| RL − RS by band | 6.4 points (0–20%) to 14.0 points (over 60%) | Footnote 6(2), p. 8 | Gap between redefined large and small groups | Number of industries in each band; significance |
| Change coefficients, Table 4 | C67 − C63: 0.21 (0.42), 0.37 (0.28), 0.29 (0.24) | Table 4, p. 9 | Association of subsequent concentration change with the gap | Any effect; all three are well within two standard errors of zero |

## Interpretation notes

- The central test is a comparison of differences, not of levels, which is the paper's main methodological advance.
  It answers a specific question (do small firms share in high returns where concentration is high) rather than the
  broader one of whether concentrated industries exercise market power.
- The 23.1% headline rests on three industries. The regression in Table 3 is the more informative statistic, and it
  explains under a tenth of the variation in the gap.
- The theoretical argument assumes a common price and constant returns. Under product differentiation, or collusion
  that leaves larger firms with lower costs, a size gap and collusion can coexist, so the evidence is against
  collusion that benefits all firms equally, not against market power in general.
- Concentration and returns are measured in the same year. A good year for large firms raises both their sales share
  and their return, which can create a positive association without any persistent efficiency difference.
- Accounting returns on book assets depend on accounting conventions that differ by firm size (owner salaries in small
  firms, historical-cost assets and acquired goodwill in large ones). The administrative-salary check addresses only
  one of these.

## Unanswered questions

- Which 95 IRS industries were used, and how were Census four-digit concentration ratios converted to the three-digit
  IRS level?
- Is "profit" before or after federal income tax, and are dividends received from other corporations included?
- How many industries entered each regression, and how many were dropped for lacking firms over $50 million?
- Which three industries make up the "over 60%" band?
- How were withheld or combined IRS cells treated?
- Why is the asset-weighted R1 for the 50–60% band (0.9%) so much lower than the unweighted figure (6.7%)?

## Items requiring expert verification

- Every value in the extraction table above was transcribed from one scanned copy of the article. They have not been
  checked against a second copy or the printed journal, and should be before they are cited.
- In the copy I read, the Table 4 regression for R4 − R1 prints an intercept of 1.5, while Table 3 prints −1.4 for the
  same dependent variable with one fewer regressor. Whether this is a lost minus sign in the scan, a typographical
  error in the original, or a genuine difference should be checked against a printed copy.
- The Table 3 significance legend is partly illegible in the scan; whether the R4 − R2 and R4 − R3 slopes are
  significant at 5% (as the double stars suggest) should be confirmed.
- I found no published correction or comment documenting an analytical error in the paper, and none is asserted here.
  The concerns above are reporting gaps and design limitations.
- The modern rerun in this repository uses the same IRS series for 2007, 2012 and 2013 with 2007 and 2012 Census
  concentration ratios. It cannot reproduce the 1963 figures, because the 1963 industry list and matching are not
  documented. It finds a 2012 slope for R4 − R1 of 0.250 (conventional s.e. 0.097) in 58 industries, but produced by
  falling small-firm returns rather than rising large-firm returns, and smaller, insignificant slopes in 2007 and 2013.
  It is a related test on later data, not a replication of the original numbers.
