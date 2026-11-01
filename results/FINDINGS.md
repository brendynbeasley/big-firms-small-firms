# Demsetz (1973) on modern data: findings

## In plain English

In 1973 Harold Demsetz showed that in American manufacturing industries dominated by four firms, the largest
companies earned far more on their assets than the smallest, while the smallest earned no more than small firms in
competitive industries. He read this as efficiency, not collusion. This rerun uses the same IRS tax tables for 2007,
2012 and 2013 and the 2017 and 2022 Economic Census.

- **The giants no longer stand out.** In 2012 the largest manufacturers averaged 4.7% to 7.1% on assets in every
  concentration band. The most concentrated industries, breweries (Anheuser-Busch InBev, MillerCoors), soft drinks
  (Coca-Cola, PepsiCo) and aerospace (Boeing, Lockheed Martin), gave their largest firms 4.7%, 10.2% and 5.4%.
- **Demsetz's slope survives, by a different route.** The gap between the largest and smallest firms widens by
  0.25 points per point of concentration in 2012, close to his 0.21, because small firms earn less in concentrated
  industries. Collusion would predict the reverse. The single-year result is fragile; the direction holds in all
  three years.
- **Leaders spend less on payroll per sales dollar almost everywhere.** In 82% of industries in 2022 the top four
  firms spent a smaller share of revenue on payroll than their rivals (Verizon, AT&T and T-Mobile 7.2% against 16.6%
  for smaller carriers), at every level of concentration. Airlines (Delta, American, United, Southwest) are an
  exception.
- **The 2017 to 2022 change result is arithmetic.** Revenue sits in both the concentration ratio and the payroll
  share, and measuring concentration by employment reverses the sign.

**Key to the labels.** *R1 to R4* are (net income + interest paid) / total assets, in percent, for corporations with
assets under $5M, $5–50M, $50–500M and over $500M ("real" scheme, Demsetz's 1963 edges scaled by CPI) or under
$0.5M, $0.5–5M, $5–50M and over $50M ("nominal", his dollar edges). *R* is the simple average of R1 to R4, as in
his tables. *CR4* is the four-firm concentration ratio in percent. *cr4_6digit* is the shipment-weighted average of
6-digit CR4s. *d_cr4* is the change in CR4 from 2007 to 2012. *Unweighted* averages industries equally;
*asset-weighted* pools profits and assets across industries (Demsetz's Table 2). In the extension, *payroll share* is
annual payroll / revenue, *gap* is the rest's share minus the top four's, *productivity ratio* is the top four's
revenue per employee over the rest's, and *wage ratio* the same for payroll per employee.

## Demsetz's tables, 1963 (from the paper)

| CR4 | Industries | R1 | R2 | R3 | R4 | R |
|---|---|---|---|---|---|---|
| 10-20% | 14 | 6.7 | 9.0 | 10.8 | 10.3 | 9.2 |
| 20-30% | 22 | 4.5 | 9.1 | 9.7 | 10.4 | 8.4 |
| 30-40% | 24 | 5.2 | 8.7 | 9.9 | 11.0 | 8.7 |
| 40-50% | 21 | 5.8 | 9.0 | 9.5 | 9.0 | 8.3 |
| 50-60% | 11 | 6.7 | 9.8 | 10.5 | 13.4 | 10.1 |
| over 60% | 3 | 5.3 | 10.1 | 11.5 | 23.1 | 12.5 |

Table 3: R4 − R1 = −1.4 + 0.21 C63 (0.07), r² = 0.09; R4 − R2 = −2.6 + 0.12 C63 (0.06), r² = 0.04;
R4 − R3 = −3.1 + 0.10 C63 (0.05), r² = 0.04. All values are in `paper_tables.csv`.

## Tables 1 and 2 rebuilt, tax year 2012 with the 2012 Census (main run)

Unweighted (Table 1):

| cr_class | industries | R1 | R2 | R3 | R4 | R |
|---|---|---|---|---|---|---|
| under 10% | 8 | 15.3 | 11.6 | 8.0 | 4.7 | 9.9 |
| 10-20% | 7 | 14.2 | 9.0 | 6.9 | 6.4 | 9.1 |
| 20-30% | 19 | 10.4 | 9.3 | 6.2 | 5.3 | 7.8 |
| 30-40% | 9 | 1.1 | 7.7 | 6.5 | 5.9 | 5.3 |
| 40-50% | 9 | 3.1 | 9.7 | 6.7 | 6.1 | 6.4 |
| 50-60% | 3 | 0.8 | 5.8 | 7.2 | 7.1 | 5.2 |
| over 60% | 3 | 7.9 | 11.3 | 9.4 | 6.7 | 8.8 |


Asset-weighted (Table 2):

| cr_class | industries | R1 | R2 | R3 | R4 | R |
|---|---|---|---|---|---|---|
| under 10% | 8 | 15.4 | 11.7 | 8.6 | 3.5 | 9.8 |
| 10-20% | 7 | 12.4 | 7.4 | 5.8 | 5.1 | 7.7 |
| 20-30% | 19 | 11.3 | 9.4 | 6.0 | 4.7 | 7.8 |
| 30-40% | 9 | 3.7 | 5.4 | 5.2 | 5.4 | 4.9 |
| 40-50% | 9 | 10.8 | 10.2 | 6.8 | 6.7 | 8.6 |
| 50-60% | 3 | 0.9 | 5.3 | 7.6 | 5.0 | 4.7 |
| over 60% | 3 | 13.2 | 10.3 | 8.5 | 5.8 | 9.4 |


## Checks: other years and Demsetz's nominal size classes

Tax year 2013 with the 2012 Census, unweighted:

| cr_class | industries | R1 | R2 | R3 | R4 | R |
|---|---|---|---|---|---|---|
| under 10% | 7 | 15.0 | 11.7 | 8.6 | 4.1 | 9.8 |
| 10-20% | 9 | 10.5 | 8.6 | 6.6 | 6.5 | 8.1 |
| 20-30% | 19 | 9.1 | 9.0 | 6.4 | 5.8 | 7.6 |
| 30-40% | 9 | 8.9 | 7.8 | 5.6 | 6.9 | 7.3 |
| 40-50% | 9 | 9.3 | 7.3 | 5.8 | 5.4 | 7.0 |
| 50-60% | 3 | 5.8 | 6.9 | 6.7 | 7.9 | 6.8 |
| over 60% | 2 | 22.1 | 10.0 | 5.8 | 9.4 | 11.8 |


Tax year 2007 with the 2007 Census, unweighted:

| cr_class | industries | R1 | R2 | R3 | R4 | R |
|---|---|---|---|---|---|---|
| under 10% | 8 | 10.7 | 10.4 | 8.4 | 6.6 | 9.0 |
| 10-20% | 13 | 10.9 | 8.7 | 7.6 | 5.9 | 8.3 |
| 20-30% | 12 | 5.4 | 7.8 | 8.0 | 7.0 | 7.0 |
| 30-40% | 13 | 10.2 | 7.6 | 7.3 | 5.6 | 7.7 |
| 40-50% | 9 | 10.9 | 6.3 | 7.5 | 8.2 | 8.2 |
| 50-60% | 3 | 8.9 | 11.3 | 6.7 | 9.1 | 9.0 |
| over 60% | 2 | 3.5 | 2.6 | 8.4 | 9.1 | 5.9 |


Tax year 2012, nominal size classes, unweighted. The R1 class (under $500,000 of assets) has tiny denominators, which is why the scaled classes are the main run:

| cr_class | industries | R1 | R2 | R3 | R4 | R |
|---|---|---|---|---|---|---|
| under 10% | 8 | 21.8 | 13.6 | 11.6 | 5.2 | 13.1 |
| 10-20% | 7 | 12.6 | 12.9 | 9.2 | 7.9 | 10.6 |
| 20-30% | 18 | -90.7 | 9.7 | 9.1 | 5.4 | -16.6 |
| 30-40% | 7 | -294.5 | 0.9 | 7.3 | 6.2 | -70.0 |
| 40-50% | 7 | -80.7 | 3.5 | 10.5 | 6.5 | -15.0 |
| 50-60% | 3 | -128.3 | 5.2 | 5.8 | 7.0 | -27.6 |
| over 60% | 3 | 19.3 | 5.0 | 11.3 | 6.7 | 10.6 |


Asset-weighted versions for 2013, 2007 and the nominal scheme are in `demsetz_tables.csv`.

## Table 3 and Table 4 rebuilt: every regression

*se* and *p* are conventional (as in the paper); *se_hc1* and *p_hc1* are heteroskedasticity-robust. Pooled rows stack 2007, 2012 and 2013 with year effects and standard errors clustered by industry. "with change" rows add d_cr4 (Table 4); for those rows the intercept and r2 are shared by the two regressors. "2012 no folded cells" drops the one industry whose withheld cell the IRS folded across a size boundary. "2012 no deleted cells in R1 or R4" drops the seven industries where the IRS deleted a cell for disclosure inside the smallest or largest class, so that R1 or R4 was built from part of the class (two textile industries, iron and steel, nonferrous metals, two electrical equipment industries, and wineries and distilleries).

| year | scheme | dependent | regressor | n | intercept | coef | se | p | se_hc1 | p_hc1 | r2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2012 | real | R4-R1 | cr4 | 58 | -10.003 | 0.250 | 0.097 | 0.012 | 0.142 | 0.080 | 0.107 |
| 2012 | real | R4-R2 | cr4 | 58 | -4.875 | 0.043 | 0.042 | 0.306 | 0.040 | 0.274 | 0.019 |
| 2012 | real | R4-R3 | cr4 | 58 | -1.373 | 0.008 | 0.025 | 0.759 | 0.034 | 0.819 | 0.002 |
| 2012 | real | R1 | cr4 | 58 | 14.938 | -0.223 | 0.093 | 0.020 | 0.130 | 0.088 | 0.092 |
| 2012 | real | R4 | cr4 | 58 | 4.935 | 0.027 | 0.020 | 0.183 | 0.021 | 0.190 | 0.031 |
| 2012 | real | R4-R1 (after tax) | cr4 | 58 | -10.053 | 0.239 | 0.096 | 0.016 | 0.140 | 0.089 | 0.099 |
| 2012 | real | R4-R1 (6-digit CR4) | cr4_6digit | 58 | -14.747 | 0.286 | 0.107 | 0.010 | 0.147 | 0.052 | 0.113 |
| 2012 | real | R4-R1 with change | cr4 | 58 | -10.176 | 0.254 | 0.098 | 0.012 | 0.146 | 0.081 | 0.109 |
| 2012 | real | R4-R1 with change | d_cr4 | 58 | -10.176 | -0.096 | 0.272 | 0.725 | 0.337 | 0.776 | 0.109 |
| 2012 | real | R4-R2 with change | cr4 | 58 | -5.120 | 0.049 | 0.042 | 0.247 | 0.043 | 0.248 | 0.042 |
| 2012 | real | R4-R2 with change | d_cr4 | 58 | -5.120 | -0.135 | 0.117 | 0.253 | 0.114 | 0.237 | 0.042 |
| 2012 | real | R4-R3 with change | cr4 | 58 | -1.616 | 0.014 | 0.025 | 0.582 | 0.037 | 0.709 | 0.067 |
| 2012 | real | R4-R3 with change | d_cr4 | 58 | -1.616 | -0.134 | 0.069 | 0.056 | 0.065 | 0.038 | 0.067 |
| 2012 no folded cells | real | R4-R1 | cr4 | 57 | -10.177 | 0.251 | 0.097 | 0.012 | 0.142 | 0.078 | 0.108 |
| 2012 no folded cells | real | R4-R2 | cr4 | 57 | -4.830 | 0.043 | 0.042 | 0.312 | 0.040 | 0.279 | 0.019 |
| 2012 no folded cells | real | R4-R3 | cr4 | 57 | -1.383 | 0.008 | 0.025 | 0.759 | 0.034 | 0.817 | 0.002 |
| 2012 no folded cells | real | R1 | cr4 | 57 | 15.090 | -0.223 | 0.094 | 0.021 | 0.130 | 0.086 | 0.094 |
| 2012 no folded cells | real | R4 | cr4 | 57 | 4.913 | 0.027 | 0.020 | 0.184 | 0.021 | 0.188 | 0.032 |
| 2012 no folded cells | real | R4-R1 (after tax) | cr4 | 57 | -10.221 | 0.240 | 0.097 | 0.016 | 0.140 | 0.087 | 0.100 |
| 2012 no folded cells | real | R4-R1 (6-digit CR4) | cr4_6digit | 57 | -14.963 | 0.288 | 0.107 | 0.010 | 0.147 | 0.051 | 0.115 |
| 2012 no folded cells | real | R4-R1 with change | cr4 | 57 | -10.463 | 0.257 | 0.098 | 0.012 | 0.146 | 0.078 | 0.113 |
| 2012 no folded cells | real | R4-R1 with change | d_cr4 | 57 | -10.463 | -0.143 | 0.279 | 0.611 | 0.332 | 0.667 | 0.113 |
| 2012 no folded cells | real | R4-R2 with change | cr4 | 57 | -5.092 | 0.049 | 0.043 | 0.254 | 0.043 | 0.253 | 0.039 |
| 2012 no folded cells | real | R4-R2 with change | d_cr4 | 57 | -5.092 | -0.131 | 0.121 | 0.285 | 0.122 | 0.283 | 0.039 |
| 2012 no folded cells | real | R4-R3 with change | cr4 | 57 | -1.670 | 0.014 | 0.025 | 0.568 | 0.037 | 0.697 | 0.072 |
| 2012 no folded cells | real | R4-R3 with change | d_cr4 | 57 | -1.670 | -0.143 | 0.071 | 0.048 | 0.065 | 0.027 | 0.072 |
| 2012 no deleted cells in R1 or R4 | real | R4-R1 | cr4 | 51 | -10.601 | 0.276 | 0.103 | 0.010 | 0.158 | 0.082 | 0.127 |
| 2012 no deleted cells in R1 or R4 | real | R4-R2 | cr4 | 51 | -4.721 | 0.038 | 0.046 | 0.409 | 0.041 | 0.353 | 0.014 |
| 2012 no deleted cells in R1 or R4 | real | R4-R3 | cr4 | 51 | -1.337 | 0.003 | 0.028 | 0.927 | 0.035 | 0.943 | 0.000 |
| 2012 no deleted cells in R1 or R4 | real | R1 | cr4 | 51 | 15.762 | -0.250 | 0.100 | 0.016 | 0.145 | 0.084 | 0.113 |
| 2012 no deleted cells in R1 or R4 | real | R4 | cr4 | 51 | 5.161 | 0.025 | 0.021 | 0.241 | 0.022 | 0.249 | 0.028 |
| 2012 no deleted cells in R1 or R4 | real | R4-R1 (after tax) | cr4 | 51 | -10.736 | 0.267 | 0.103 | 0.012 | 0.156 | 0.087 | 0.121 |
| 2012 no deleted cells in R1 or R4 | real | R4-R1 (6-digit CR4) | cr4_6digit | 51 | -14.854 | 0.293 | 0.112 | 0.012 | 0.152 | 0.055 | 0.123 |
| 2012 no deleted cells in R1 or R4 | real | R4-R1 with change | cr4 | 51 | -10.962 | 0.285 | 0.105 | 0.009 | 0.164 | 0.083 | 0.135 |
| 2012 no deleted cells in R1 or R4 | real | R4-R1 with change | d_cr4 | 51 | -10.962 | -0.192 | 0.291 | 0.513 | 0.314 | 0.542 | 0.135 |
| 2012 no deleted cells in R1 or R4 | real | R4-R2 with change | cr4 | 51 | -5.003 | 0.045 | 0.046 | 0.330 | 0.045 | 0.313 | 0.042 |
| 2012 no deleted cells in R1 or R4 | real | R4-R2 with change | d_cr4 | 51 | -5.003 | -0.150 | 0.128 | 0.245 | 0.117 | 0.200 | 0.042 |
| 2012 no deleted cells in R1 or R4 | real | R4-R3 with change | cr4 | 51 | -1.601 | 0.009 | 0.027 | 0.737 | 0.038 | 0.812 | 0.068 |
| 2012 no deleted cells in R1 or R4 | real | R4-R3 with change | d_cr4 | 51 | -1.601 | -0.141 | 0.075 | 0.069 | 0.070 | 0.045 | 0.068 |
| 2012 | nominal | R4-R1 | cr4 | 53 | 19.178 | 2.355 | 3.562 | 0.511 | 2.388 | 0.324 | 0.009 |
| 2012 | nominal | R4-R2 | cr4 | 53 | -7.315 | 0.179 | 0.090 | 0.052 | 0.138 | 0.194 | 0.072 |
| 2012 | nominal | R4-R3 | cr4 | 53 | -3.968 | 0.025 | 0.043 | 0.565 | 0.038 | 0.512 | 0.007 |
| 2012 | nominal | R1 | cr4 | 53 | -13.389 | -2.344 | 3.561 | 0.513 | 2.385 | 0.326 | 0.008 |
| 2012 | nominal | R4 | cr4 | 53 | 5.790 | 0.011 | 0.021 | 0.593 | 0.020 | 0.586 | 0.006 |
| 2012 | nominal | R4-R1 (after tax) | cr4 | 53 | 19.252 | 2.339 | 3.562 | 0.514 | 2.388 | 0.327 | 0.008 |
| 2012 | nominal | R4-R1 (6-digit CR4) | cr4_6digit | 53 | 62.481 | 0.606 | 3.894 | 0.877 | 1.834 | 0.741 | 0.000 |
| 2012 | nominal | R4-R1 with change | cr4 | 53 | 36.503 | 1.953 | 3.592 | 0.589 | 2.344 | 0.405 | 0.026 |
| 2012 | nominal | R4-R1 with change | d_cr4 | 53 | 36.503 | 9.439 | 10.102 | 0.355 | 10.046 | 0.347 | 0.026 |
| 2012 | nominal | R4-R2 with change | cr4 | 53 | -7.567 | 0.185 | 0.091 | 0.048 | 0.142 | 0.192 | 0.077 |
| 2012 | nominal | R4-R2 with change | d_cr4 | 53 | -7.567 | -0.137 | 0.257 | 0.596 | 0.325 | 0.673 | 0.077 |
| 2012 | nominal | R4-R3 with change | cr4 | 53 | -4.183 | 0.030 | 0.043 | 0.493 | 0.041 | 0.464 | 0.025 |
| 2012 | nominal | R4-R3 with change | d_cr4 | 53 | -4.183 | -0.117 | 0.121 | 0.336 | 0.121 | 0.332 | 0.025 |
| 2013 | real | R4-R1 | cr4 | 58 | -7.950 | 0.129 | 0.105 | 0.222 | 0.104 | 0.214 | 0.027 |
| 2013 | real | R4-R2 | cr4 | 58 | -5.842 | 0.111 | 0.052 | 0.038 | 0.052 | 0.033 | 0.075 |
| 2013 | real | R4-R3 | cr4 | 58 | -3.197 | 0.097 | 0.034 | 0.006 | 0.036 | 0.007 | 0.127 |
| 2013 | real | R1 | cr4 | 58 | 12.541 | -0.079 | 0.100 | 0.433 | 0.104 | 0.450 | 0.011 |
| 2013 | real | R4 | cr4 | 58 | 4.590 | 0.051 | 0.027 | 0.061 | 0.030 | 0.087 | 0.061 |
| 2013 | real | R4-R1 (after tax) | cr4 | 58 | -8.300 | 0.125 | 0.101 | 0.220 | 0.098 | 0.199 | 0.027 |
| 2013 | real | R4-R1 (6-digit CR4) | cr4_6digit | 58 | -8.800 | 0.109 | 0.112 | 0.336 | 0.096 | 0.257 | 0.017 |
| 2013 | real | R4-R1 with change | cr4 | 58 | -9.063 | 0.161 | 0.103 | 0.123 | 0.099 | 0.104 | 0.102 |
| 2013 | real | R4-R1 with change | d_cr4 | 58 | -9.063 | -0.537 | 0.251 | 0.037 | 0.188 | 0.004 | 0.102 |
| 2013 | real | R4-R2 with change | cr4 | 58 | -6.160 | 0.120 | 0.052 | 0.026 | 0.054 | 0.027 | 0.098 |
| 2013 | real | R4-R2 with change | d_cr4 | 58 | -6.160 | -0.153 | 0.128 | 0.237 | 0.154 | 0.321 | 0.098 |
| 2013 | real | R4-R3 with change | cr4 | 58 | -3.401 | 0.102 | 0.034 | 0.004 | 0.037 | 0.005 | 0.149 |
| 2013 | real | R4-R3 with change | d_cr4 | 58 | -3.401 | -0.098 | 0.083 | 0.243 | 0.074 | 0.183 | 0.149 |
| 2013 | nominal | R4-R1 | cr4 | 47 | -17.441 | 0.756 | 0.900 | 0.405 | 1.191 | 0.526 | 0.015 |
| 2013 | nominal | R4-R2 | cr4 | 47 | -6.305 | 0.105 | 0.136 | 0.446 | 0.103 | 0.310 | 0.013 |
| 2013 | nominal | R4-R3 | cr4 | 47 | -4.379 | 0.048 | 0.054 | 0.379 | 0.046 | 0.299 | 0.017 |
| 2013 | nominal | R1 | cr4 | 47 | 22.948 | -0.734 | 0.901 | 0.419 | 1.192 | 0.538 | 0.015 |
| 2013 | nominal | R4 | cr4 | 47 | 5.507 | 0.022 | 0.022 | 0.320 | 0.020 | 0.277 | 0.022 |
| 2013 | nominal | R4-R1 (after tax) | cr4 | 47 | -17.817 | 0.744 | 0.898 | 0.412 | 1.191 | 0.532 | 0.015 |
| 2013 | nominal | R4-R1 (6-digit CR4) | cr4_6digit | 47 | -2.517 | 0.121 | 0.934 | 0.897 | 0.939 | 0.897 | 0.000 |
| 2013 | nominal | R4-R1 with change | cr4 | 47 | -20.671 | 0.817 | 0.889 | 0.363 | 1.180 | 0.489 | 0.061 |
| 2013 | nominal | R4-R1 with change | d_cr4 | 47 | -20.671 | -3.212 | 2.191 | 0.150 | 1.131 | 0.005 | 0.061 |
| 2013 | nominal | R4-R2 with change | cr4 | 47 | -6.912 | 0.116 | 0.133 | 0.386 | 0.107 | 0.276 | 0.084 |
| 2013 | nominal | R4-R2 with change | d_cr4 | 47 | -6.912 | -0.603 | 0.327 | 0.072 | 0.226 | 0.008 | 0.084 |
| 2013 | nominal | R4-R3 with change | cr4 | 47 | -4.622 | 0.053 | 0.053 | 0.323 | 0.045 | 0.244 | 0.088 |
| 2013 | nominal | R4-R3 with change | d_cr4 | 47 | -4.622 | -0.241 | 0.130 | 0.071 | 0.132 | 0.068 | 0.088 |
| 2007 | real | R4-R1 | cr4 | 60 | -5.207 | 0.093 | 0.103 | 0.368 | 0.081 | 0.249 | 0.014 |
| 2007 | real | R4-R2 | cr4 | 60 | -4.768 | 0.119 | 0.049 | 0.018 | 0.046 | 0.010 | 0.093 |
| 2007 | real | R4-R3 | cr4 | 60 | -2.655 | 0.060 | 0.032 | 0.067 | 0.035 | 0.083 | 0.057 |
| 2007 | real | R1 | cr4 | 60 | 10.315 | -0.036 | 0.101 | 0.724 | 0.083 | 0.666 | 0.002 |
| 2007 | real | R4 | cr4 | 60 | 5.108 | 0.057 | 0.027 | 0.042 | 0.025 | 0.021 | 0.069 |
| 2007 | real | R4-R1 (after tax) | cr4 | 60 | -5.617 | 0.095 | 0.102 | 0.354 | 0.080 | 0.231 | 0.015 |
| 2007 | real | R4-R1 (6-digit CR4) | cr4_6digit | 60 | -5.635 | 0.072 | 0.113 | 0.526 | 0.097 | 0.457 | 0.007 |
| 2007 | nominal | R4-R1 | cr4 | 53 | -10.442 | 1.047 | 0.730 | 0.158 | 0.819 | 0.201 | 0.039 |
| 2007 | nominal | R4-R2 | cr4 | 53 | -4.356 | 0.049 | 0.113 | 0.667 | 0.075 | 0.513 | 0.004 |
| 2007 | nominal | R4-R3 | cr4 | 53 | -4.103 | 0.113 | 0.048 | 0.022 | 0.048 | 0.019 | 0.099 |
| 2007 | nominal | R1 | cr4 | 53 | 16.075 | -1.000 | 0.730 | 0.177 | 0.823 | 0.225 | 0.035 |
| 2007 | nominal | R4 | cr4 | 53 | 5.632 | 0.047 | 0.026 | 0.072 | 0.025 | 0.061 | 0.062 |
| 2007 | nominal | R4-R1 (after tax) | cr4 | 53 | -11.336 | 1.058 | 0.729 | 0.153 | 0.814 | 0.194 | 0.040 |
| 2007 | nominal | R4-R1 (6-digit CR4) | cr4_6digit | 53 | -3.072 | 0.523 | 0.820 | 0.526 | 0.567 | 0.356 | 0.008 |
| pooled 2007+2012+2013 | real | R4-R1 | cr4 | 176 | -7.083 | 0.158 | 0.078 | 0.043 |  |  | 0.045 |
| pooled 2007+2012+2013 | real | R4-R2 | cr4 | 176 | -3.926 | 0.091 | 0.037 | 0.014 |  |  | 0.084 |
| pooled 2007+2012+2013 | real | R4-R3 | cr4 | 176 | -2.409 | 0.052 | 0.029 | 0.075 |  |  | 0.053 |
| pooled 2007+2012+2013 | real | R1 | cr4 | 176 | 12.548 | -0.113 | 0.072 | 0.117 |  |  | 0.027 |
| pooled 2007+2012+2013 | real | R4 | cr4 | 176 | 5.465 | 0.045 | 0.018 | 0.011 |  |  | 0.073 |


## All manufacturing by size class, 2012

return_pct is (net income + interest) / assets. intangibles are amortizable intangibles net of amortization. S-corporation assets cannot be split at $500M, so the share is shown only for R1 and R2.

| size_class | returns | assets_bn | return_pct | officer_pay_pct_assets | intangibles_pct_assets | other_investments_pct_assets | s_corp_share_assets_pct |
|---|---|---|---|---|---|---|---|
| R1 | 186,337 | 116.6 | 12.8 | 14.5 | 2.1 | 4.3 | 58.0 |
| R2 | 20,582 | 297.5 | 9.3 | 4.1 | 4.3 | 5.8 | 52.2 |
| R3 | 3,938 | 598.8 | 6.6 | 1.2 | 13.0 | 10.3 |  |
| R4 | 1,221 | 10974.1 | 5.6 | 0.2 | 12.7 | 35.7 |  |


## Industry table, 2012 (58 industries, real size classes)

shipments_bn is 2012 Census shipments in billions of dollars; firms1 and firms4 are the IRS weighted counts of returns in the smallest and largest classes. All columns, and the 2013 and 2007 versions, are in `industries_<year>.csv`.

| industry | cr4 | cr4_6digit | d_cr4 | R1 | R2 | R3 | R4 | firms1 | firms4 | shipments_bn |
|---|---|---|---|---|---|---|---|---|---|---|
| Breweries | 87.8 | 87.8 | -1.7 | 20.1 | 12.4 | 12.1 | 4.7 | 302 | 4 | 28.4 |
| Soft Drink and Ice | 62.8 | 68.5 | 11.3 | -17.8 | 12.1 | 8.6 | 10.2 | 394 | 7 | 48.6 |
| Aerospace Product and Parts | 61.0 | 75.0 | 2.9 | 21.4 | 9.4 | 7.5 | 5.4 | 996 | 34 | 209.6 |
| Other Transportation Equipment and Railroad Rolling Stock | 54.2 | 65.9 | 4.9 | 2.3 | 8.9 | 9.4 | 10.1 | 1,700 | 9 | 35.8 |
| Wineries and Distilleries | 52.8 | 52.8 | 0.7 | 0.6 | 3.4 | 4.6 | 6.3 | 1,110 | 5 | 25.1 |
| Electrical Lighting Equipment and Household Appliance | 50.6 | 53.2 | 1.1 | -0.4 | 5.0 | 7.6 | 4.8 | 881 | 13 | 31.4 |
| Ship and Boat Building | 48.6 | 53.5 | 4.2 | 4.9 | 10.4 | 8.1 | 8.6 | 544 | 4 | 32.1 |
| Petroleum Refineries (including integrated) | 46.9 | 46.9 | -0.6 | 4.1 | 14.5 | 5.9 | 7.0 | 142 | 30 | 801.9 |
| Engine, Turbine and Power Transmission Equipment | 44.4 | 56.2 | 2.4 | -35.2 | 3.9 | 4.2 | 6.0 | 144 | 13 | 54.1 |
| Animal Food and Grain and Oilseed Milling | 43.2 | 59.4 | -1.6 | 2.0 | 9.4 | 10.1 | 5.9 | 1,372 | 13 | 159.4 |
| Iron, Steel Mills and Steel Product | 43.1 | 45.8 | -1.8 | 22.2 | 10.5 | 3.7 | 4.1 | 593 | 28 | 138.5 |
| Pulp, Paper, and Paperboard Mills | 41.9 | 55.9 | 5.3 | -4.6 | 3.4 | 4.5 | 3.2 | 352 | 20 | 81.2 |
| Meat and Seafood Processing | 41.6 | 46.7 | 4.6 | 15.4 | 9.7 | 7.3 | 6.5 | 2,193 | 18 | 210.3 |
| Soap, Cleaning Compound, and Toilet Preparation | 41.3 | 58.5 | -0.9 | -3.8 | 13.9 | 7.9 | 6.6 | 1,335 | 16 | 86.8 |
| Agriculture, Construction, and Mining Machinery | 40.2 | 54.2 | 3.4 | 22.7 | 12.0 | 9.0 | 7.1 | 3,057 | 26 | 117.2 |
| Motor Vehicles and Parts | 39.6 | 53.2 | -4.7 | 9.8 | 4.6 | 4.6 | 4.1 | 4,686 | 86 | 508.2 |
| Audio and Video Equipment Mfg and Reproducing Magnetic and Optical Media | 38.5 | 41.2 | -2.0 | -6.5 | 3.1 | 1.2 | 2.5 | 871 | 6 | 5.9 |
| Rubber Product | 37.9 | 50.5 | -1.6 | 14.3 | 19.5 | 8.2 | 7.6 | 981 | 15 | 45.5 |
| Asphalt Paving, Roofing, Other Petroleum and Coal Products | 37.3 | 47.6 | 7.1 | 0.3 | 16.3 | 9.4 | 5.1 | 693 | 6 | 49.2 |
| Boiler, Tank, and Shipping Container | 32.4 | 45.0 | -0.6 | 0.3 | 11.4 | 10.2 | 8.3 | 748 | 11 | 35.1 |
| Sugar and Confectionery Product | 31.6 | 56.8 | -5.9 | 5.7 | 11.3 | 13.0 | 9.7 | 1,132 | 11 | 33.1 |
| Computer and Peripheral Equipment | 31.5 | 51.9 | -31.9 | -10.2 | 1.0 | 2.4 | 7.5 | 773 | 28 | 29.9 |
| Pharmaceutical and Medicine | 31.2 | 37.8 | 1.7 | -17.8 | -4.7 | 4.9 | 5.6 | 838 | 60 | 189.0 |
| Nonferrous Metal Production and Processing | 31.1 | 48.2 | -3.9 | 14.0 | 7.3 | 4.5 | 2.7 | 457 | 27 | 99.1 |
| Communications Equipment | 29.6 | 42.9 | -7.8 | 3.7 | 7.3 | 7.0 | 7.2 | 1,421 | 22 | 43.6 |
| Other Food | 29.5 | 48.6 | -1.9 | 6.2 | 15.2 | 9.8 | 2.0 | 2,248 | 13 | 94.5 |
| Paint, Coating, and Adhesive | 29.3 | 34.5 | 0.4 | 16.5 | 9.7 | 7.1 | 6.3 | 1,607 | 12 | 36.2 |
| Resin, Synthetic Rubber, and Artificial Synthetic Fibers and Filaments | 29.0 | 36.2 | -0.8 | 32.0 | 8.3 | 8.1 | 4.4 | 235 | 18 | 109.5 |
| Basic Chemical | 28.5 | 48.2 | -4.8 | 12.2 | 5.8 | 3.7 | 4.8 | 377 | 66 | 276.0 |
| Electrical Equipment | 27.9 | 40.2 | 8.6 | 1.6 | 12.5 | 7.4 | 6.7 | 325 | 3 | 38.9 |
| Other Chemical Product and Preparation | 27.1 | 47.5 | 0.6 | 12.1 | 11.1 | 8.4 | 10.3 | 1,605 | 24 | 87.8 |
| Ventilation, Heating, Air-Conditioning, and Commercial Refrigeration Equipment | 26.4 | 31.5 | -2.8 | -4.9 | 9.1 | 9.0 | 4.1 | 651 | 10 | 41.8 |
| Textile Product Mills | 24.8 | 35.4 | -8.0 | 8.2 | 9.1 | 3.3 | 4.3 | 1,633 | 4 | 22.1 |
| Fruit and Vegetable Preserving and Specialty Food | 24.7 | 37.3 | 3.0 | 3.4 | 12.2 | 8.3 | 4.8 | 591 | 14 | 69.9 |
| Bakeries and Tortilla Manufacturing | 24.1 | 42.3 | 1.7 | 6.1 | 9.9 | 5.5 | 5.9 | 2,697 | 15 | 64.6 |
| Glass and Glass Product | 23.9 | 47.8 | -5.2 | 7.2 | 13.8 | -1.1 | 2.5 | 1,807 | 10 | 23.2 |
| Converted Paper Product | 22.7 | 42.3 | 5.7 | 18.6 | 4.9 | 7.9 | 7.0 | 1,667 | 19 | 99.4 |
| Dairy Product | 22.2 | 40.3 | -1.3 | 9.1 | 6.0 | 10.8 | 10.3 | 1,248 | 13 | 107.4 |
| Clay, Refractory and Other Nonmetallic Mineral Product | 21.8 | 39.4 | -0.4 | 16.0 | 10.5 | 5.9 | 3.0 | 2,035 | 10 | 28.7 |
| Industrial Machinery | 21.6 | 31.6 | -1.6 | 19.7 | 10.5 | 8.0 | 6.5 | 2,519 | 16 | 32.3 |
| Semiconductor and Other Electronic Component | 20.9 | 32.6 | -13.2 | 10.6 | 7.6 | 0.0 | 6.5 | 2,828 | 76 | 90.4 |
| Textile Mills | 20.6 | 36.1 | 1.0 | 9.1 | 4.8 | 5.0 | 4.7 | 1,078 | 4 | 30.2 |
| Cement, Concrete, Lime and Gypsum Product | 20.3 | 27.5 | -4.5 | 10.6 | 8.1 | 4.0 | 0.3 | 3,329 | 27 | 47.1 |
| Medical Equipment and Supplies | 19.3 | 29.1 | 0.1 | 4.1 | -3.8 | 4.3 | 7.5 | 6,569 | 59 | 90.9 |
| Foundries | 19.0 | 35.1 | 3.4 | 20.9 | 11.9 | 9.3 | 9.1 | 1,375 | 10 | 31.9 |
| Navigational, Measuring, Electromedical, and Control Instruments | 18.8 | 41.7 | 1.1 | 7.5 | 9.9 | 7.0 | 3.9 | 2,733 | 47 | 143.7 |
| Coating, Engraving, Heat Treating, and Allied Activities | 14.2 | 24.8 | 2.3 | 18.8 | 10.4 | 8.6 | 11.5 | 2,007 | 4 | 26.9 |
| Other Electrical Equipment and Component | 12.8 | 43.6 | -0.4 | 1.6 | 8.3 | 4.6 | 2.6 | 813 | 23 | 53.3 |
| Forging and Stamping | 12.4 | 26.8 | 0.4 | 14.6 | 16.4 | 9.5 | 6.1 | 1,774 | 3 | 34.4 |
| Commercial and Service Industry Machinery | 10.9 | 19.8 | 0.1 | 31.9 | 10.0 | 4.9 | 3.8 | 1,322 | 14 | 25.1 |
| Cutlery, Hardware, Spring and Wire: Machine Shops, Nut, Bolt | 10.0 | 12.6 | 1.5 | 16.3 | 13.9 | 8.1 | 3.1 | 16,368 | 12 | 92.8 |
| Other Fabricated Metal Product | 9.9 | 32.6 | -1.5 | 19.9 | 14.8 | 12.7 | 2.2 | 11,621 | 28 | 74.6 |
| Other Miscellaneous Manufacturing | 9.4 | 28.8 | 1.3 | 15.5 | 10.0 | 8.7 | 8.9 | 18,252 | 23 | 58.3 |
| Wood Product Manufacturing | 9.2 | 25.9 | 0.1 | 10.1 | 7.7 | 4.0 | 4.7 | 9,226 | 16 | 78.1 |
| Other General Purpose Machinery | 8.9 | 36.0 | 0.6 | 17.2 | 14.3 | 9.3 | 3.2 | 3,775 | 27 | 102.2 |
| Metalworking Machinery | 8.0 | 16.9 | -1.4 | 17.5 | 13.0 | 9.2 | 5.8 | 5,466 | 6 | 29.5 |
| Plastics Product | 7.3 | 21.3 | 1.9 | 12.0 | 10.0 | 8.4 | 6.9 | 6,011 | 28 | 173.1 |
| Architectural and Structural Metals | 6.0 | 13.9 | 0.7 | 14.0 | 8.8 | 3.8 | 2.9 | 6,861 | 7 | 76.1 |


## Extension: top four against the rest, 2017 and 2022

Medians across industries by CR4 band. revenue_bn is total revenue in billions of dollars. pct_leaders_lower is the percentage of industries where the top four have the lower payroll share.

| year | cr_class | industries | revenue_bn | pay_share_top4_median | pay_share_rest_median | pay_gap_median | pct_leaders_lower | productivity_ratio_median | wage_ratio_median |
|---|---|---|---|---|---|---|---|---|---|
| 2017 | under 20% | 278 | 12,084 | 23.76 | 27.14 | 3.60 | 70.5 | 1.47 | 1.221 |
| 2017 | 20-40% | 284 | 9,795 | 14.01 | 20.11 | 4.51 | 85.2 | 1.54 | 1.130 |
| 2017 | 40-60% | 198 | 5,521 | 12.53 | 17.85 | 4.57 | 85.4 | 1.63 | 1.155 |
| 2017 | 60% and over | 124 | 3,675 | 11.02 | 16.52 | 4.55 | 84.7 | 1.61 | 1.157 |
| 2017 | all | 884 | 31,074 | 14.91 | 21.35 | 4.34 | 80.5 | 1.55 | 1.163 |
| 2022 | under 20% | 219 | 14,130 | 22.24 | 26.99 | 3.17 | 72.6 | 1.42 | 1.216 |
| 2022 | 20-40% | 274 | 12,233 | 13.25 | 18.96 | 3.95 | 84.7 | 1.53 | 1.125 |
| 2022 | 40-60% | 162 | 7,724 | 10.86 | 16.81 | 4.95 | 86.4 | 1.69 | 1.135 |
| 2022 | 60% and over | 115 | 4,405 | 11.11 | 17.31 | 5.01 | 87.0 | 1.69 | 1.117 |
| 2022 | all | 770 | 38,492 | 13.99 | 20.31 | 4.08 | 81.9 | 1.53 | 1.155 |


The twelve largest industries with CR4 of 50% or more in 2022 (pay shares in percent, revenue and pay per worker in thousands of dollars):

| naics | industry | sector | cr4 | revenue_bn | pay_share_top4 | pay_share_rest | rev_per_worker_top4 | rev_per_worker_rest | wage_top4 | wage_rest |
|---|---|---|---|---|---|---|---|---|---|---|
| 424210 | Drugs and druggists' sundries merchant wholesalers | Wholesale | 50.2 | 1280.9 | 0.6 | 6.2 | 19566.6 | 2316.0 | 113.5 | 143.1 |
| 324110 | Petroleum refineries | Manufacturing | 52.2 | 825.2 | 0.9 | 1.3 | 17195.7 | 12272.4 | 158.8 | 156.6 |
| 455211 | Warehouse clubs and supercenters | Retail | 95.5 | 810.4 | 7.8 | 8.0 | 387.1 | 475.4 | 30.3 | 38.0 |
| 423110 | Automobile and other motor vehicle merchant wholesalers | Wholesale | 51.1 | 768.3 | 0.3 | 2.8 | 54315.8 | 2779.5 | 145.3 | 77.4 |
| 456110 | Pharmacies and drug retailers | Retail | 71.0 | 543.9 | 5.1 | 8.0 | 824.0 | 616.4 | 41.6 | 49.1 |
| 336110 | Automobile and light duty motor vehicle manufacturing | Manufacturing | 58.3 | 357.2 | 4.6 | 4.9 | 1753.1 | 1574.7 | 79.8 | 77.4 |
| 517111 | Wired telecommunications carriers | Information | 65.4 | 322.7 | 15.3 | 18.9 | 574.0 | 420.1 | 87.6 | 79.5 |
| 517112 | Wireless telecommunications carriers (except satellite) | Information | 96.5 | 283.0 | 7.2 | 16.6 | 1184.4 | 280.1 | 85.5 | 46.4 |
| 444110 | Home centers | Retail | 98.0 | 258.0 | 8.4 | 10.9 | 344.5 | 348.4 | 29.0 | 38.0 |
| 481111 | Scheduled passenger air transportation | Transportation | 72.9 | 228.9 | 19.6 | 13.9 | 480.4 | 543.2 | 94.2 | 75.4 |
| 457120 | Other gasoline stations | Retail | 60.6 | 187.8 | 2.0 | 4.0 | 1518.0 | 781.6 | 30.1 | 31.4 |
| 424940 | Tobacco product and electronic cigarette merchant wholesalers | Wholesale | 56.2 | 143.6 | 1.8 | 3.3 | 3317.7 | 1884.3 | 59.4 | 61.5 |


Every extension regression (HC1 standard errors). "all sectors" rows include sector effects. emp_share4 is the top four's share of employment; d_ is the 2017 to 2022 change for the 696 industries with the same code in both years.

| test | sample | weights | dependent | regressor | n | coef | se | p | r2 |
|---|---|---|---|---|---|---|---|---|---|
| levels 2017 | all sectors | equal | pay_gap | cr4 | 884 | 0.0032 | 0.0144 | 0.8215 | 0.0455 |
| levels 2017 | all sectors | revenue | pay_gap | cr4 | 884 | -0.0167 | 0.0153 | 0.2754 | 0.1052 |
| levels 2017 | manufacturing | equal | pay_gap | cr4 | 358 | -0.0221 | 0.0188 | 0.2404 | 0.0067 |
| levels 2017 | manufacturing | revenue | pay_gap | cr4 | 358 | -0.0154 | 0.0271 | 0.5698 | 0.0050 |
| levels 2017 | all sectors | equal | log_productivity_ratio | cr4 | 884 | 0.0022 | 0.0009 | 0.0110 | 0.1834 |
| levels 2017 | all sectors | revenue | log_productivity_ratio | cr4 | 884 | 0.0046 | 0.0025 | 0.0709 | 0.3701 |
| levels 2017 | manufacturing | equal | log_productivity_ratio | cr4 | 358 | 0.0022 | 0.0013 | 0.0885 | 0.0122 |
| levels 2017 | manufacturing | revenue | log_productivity_ratio | cr4 | 358 | 0.0030 | 0.0025 | 0.2424 | 0.0234 |
| levels 2017 | all sectors | equal | log_wage_ratio | cr4 | 884 | 0.0000 | 0.0005 | 0.9744 | 0.1316 |
| levels 2017 | all sectors | revenue | log_wage_ratio | cr4 | 884 | -0.0002 | 0.0015 | 0.8713 | 0.0803 |
| levels 2017 | manufacturing | equal | log_wage_ratio | cr4 | 358 | 0.0006 | 0.0004 | 0.1724 | 0.0054 |
| levels 2017 | manufacturing | revenue | log_wage_ratio | cr4 | 358 | 0.0005 | 0.0007 | 0.4648 | 0.0048 |
| levels 2017 | all sectors | equal | pay_gap | emp_share4 | 884 | -0.0775 | 0.0170 | 0.0000 | 0.0781 |
| levels 2022 | all sectors | equal | pay_gap | cr4 | 770 | 0.0141 | 0.0161 | 0.3829 | 0.0349 |
| levels 2022 | all sectors | revenue | pay_gap | cr4 | 770 | -0.0024 | 0.0156 | 0.8755 | 0.0941 |
| levels 2022 | manufacturing | equal | pay_gap | cr4 | 344 | 0.0059 | 0.0199 | 0.7681 | 0.0005 |
| levels 2022 | manufacturing | revenue | pay_gap | cr4 | 344 | -0.0159 | 0.0204 | 0.4362 | 0.0046 |
| levels 2022 | all sectors | equal | log_productivity_ratio | cr4 | 770 | 0.0022 | 0.0009 | 0.0138 | 0.1425 |
| levels 2022 | all sectors | revenue | log_productivity_ratio | cr4 | 770 | 0.0020 | 0.0029 | 0.4788 | 0.3685 |
| levels 2022 | manufacturing | equal | log_productivity_ratio | cr4 | 344 | 0.0034 | 0.0012 | 0.0038 | 0.0245 |
| levels 2022 | manufacturing | revenue | log_productivity_ratio | cr4 | 344 | 0.0027 | 0.0022 | 0.2096 | 0.0132 |
| levels 2022 | all sectors | equal | log_wage_ratio | cr4 | 770 | -0.0006 | 0.0004 | 0.1387 | 0.1286 |
| levels 2022 | all sectors | revenue | log_wage_ratio | cr4 | 770 | -0.0018 | 0.0011 | 0.0970 | 0.1479 |
| levels 2022 | manufacturing | equal | log_wage_ratio | cr4 | 344 | 0.0003 | 0.0005 | 0.5539 | 0.0010 |
| levels 2022 | manufacturing | revenue | log_wage_ratio | cr4 | 344 | 0.0001 | 0.0008 | 0.8539 | 0.0002 |
| levels 2022 | all sectors | equal | pay_gap | emp_share4 | 770 | -0.0723 | 0.0210 | 0.0006 | 0.0622 |
| changes 2017-2022 | all sectors | equal | d_pay_gap | d_cr4 | 696 | 0.2213 | 0.0403 | 0.0000 | 0.0924 |
| changes 2017-2022 | all sectors | revenue | d_pay_gap | d_cr4 | 696 | 0.1809 | 0.0592 | 0.0022 | 0.1231 |
| changes 2017-2022 | manufacturing | equal | d_pay_gap | d_cr4 | 326 | 0.2069 | 0.0365 | 0.0000 | 0.0947 |
| changes 2017-2022 | manufacturing | revenue | d_pay_gap | d_cr4 | 326 | 0.1702 | 0.0506 | 0.0008 | 0.0761 |
| changes 2017-2022 | all sectors | equal | d_log_productivity_ratio | d_cr4 | 696 | 0.0175 | 0.0027 | 0.0000 | 0.1478 |
| changes 2017-2022 | all sectors | revenue | d_log_productivity_ratio | d_cr4 | 696 | 0.0137 | 0.0051 | 0.0071 | 0.2924 |
| changes 2017-2022 | manufacturing | equal | d_log_productivity_ratio | d_cr4 | 326 | 0.0194 | 0.0029 | 0.0000 | 0.1776 |
| changes 2017-2022 | manufacturing | revenue | d_log_productivity_ratio | d_cr4 | 326 | 0.0167 | 0.0063 | 0.0080 | 0.1181 |
| changes 2017-2022 | all sectors | equal | d_log_wage_ratio | d_cr4 | 696 | 0.0019 | 0.0021 | 0.3737 | 0.0312 |
| changes 2017-2022 | all sectors | revenue | d_log_wage_ratio | d_cr4 | 696 | 0.0036 | 0.0033 | 0.2654 | 0.1654 |
| changes 2017-2022 | manufacturing | equal | d_log_wage_ratio | d_cr4 | 326 | 0.0001 | 0.0015 | 0.9534 | 0.0000 |
| changes 2017-2022 | manufacturing | revenue | d_log_wage_ratio | d_cr4 | 326 | -0.0009 | 0.0018 | 0.6203 | 0.0016 |
| changes 2017-2022 | all sectors | equal | d_pay_gap | d_emp_share4 | 696 | -0.2472 | 0.0548 | 0.0000 | 0.0957 |
| changes 2017-2022 | all sectors | revenue | d_pay_gap | d_emp_share4 | 696 | -0.2695 | 0.0630 | 0.0000 | 0.1570 |
| changes 2017-2022 | manufacturing | equal | d_pay_gap | d_emp_share4 | 326 | -0.1624 | 0.0348 | 0.0000 | 0.0505 |
| changes 2017-2022 | manufacturing | revenue | d_pay_gap | d_emp_share4 | 326 | -0.1241 | 0.0357 | 0.0005 | 0.0419 |
| changes 2017-2022 | all sectors | equal | d_log_productivity_ratio | d_emp_share4 | 696 | -0.0255 | 0.0022 | 0.0000 | 0.2357 |
| changes 2017-2022 | all sectors | revenue | d_log_productivity_ratio | d_emp_share4 | 696 | -0.0355 | 0.0042 | 0.0000 | 0.4679 |
| changes 2017-2022 | manufacturing | equal | d_log_productivity_ratio | d_emp_share4 | 326 | -0.0190 | 0.0027 | 0.0000 | 0.1470 |
| changes 2017-2022 | manufacturing | revenue | d_log_productivity_ratio | d_emp_share4 | 326 | -0.0212 | 0.0042 | 0.0000 | 0.1963 |
| changes 2017-2022 | all sectors | equal | d_log_wage_ratio | d_emp_share4 | 696 | -0.0110 | 0.0023 | 0.0000 | 0.1206 |
| changes 2017-2022 | all sectors | revenue | d_log_wage_ratio | d_emp_share4 | 696 | -0.0117 | 0.0031 | 0.0001 | 0.2217 |
| changes 2017-2022 | manufacturing | equal | d_log_wage_ratio | d_emp_share4 | 326 | -0.0045 | 0.0019 | 0.0188 | 0.0298 |
| changes 2017-2022 | manufacturing | revenue | d_log_wage_ratio | d_emp_share4 | 326 | -0.0051 | 0.0016 | 0.0015 | 0.0554 |

## How to read this

The rebuilt tables support Demsetz's narrower claim, that small firms in concentrated industries do not earn the
premium collusion would hand them, and not his broader picture of highly profitable leaders in concentrated
industries. The single-year slope matches his but is significant only with conventional errors, and in 2013 and 2007
the R4 − R1 slope is smaller and insignificant while the R4 − R2 and R4 − R3 slopes are significant. Tax-return
balance sheets are consolidated, so the largest corporations' assets include investments in other companies (36% of
the largest class's assets in 2012) and acquired intangibles (13%), which depresses their measured return. Small
corporations' returns depend on how owners split pay and profit, and 58% of small-firm assets are in S corporations.
The census extension measures payroll and productivity rather than profit.

## Sample

| | 2007 | 2012 | 2013 |
|---|---|---|---|
| IRS manufacturing industries | 64 | 64 | 64 |
| Kept (all four size classes and a CR4) | 60 | 58 | 58 |
| Concentration year | 2007 | 2012 | 2012 |

Extension: 884 industries kept of 943 in 2017 and 770 of 899 in 2022 (finance dropped, withheld or flagged values
dropped, at least 8 firms), 696 matched across the two years.

Data: IRS SOI Corporation Source Book flat files (2007, 2012, 2013); Census Bureau Economic Census concentration
tables (2007, 2012, 2017, 2022); CPI-U from FRED. Downloaded 2026-11-01.
