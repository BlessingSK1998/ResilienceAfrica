# Resilience and Development in Sub-Saharan Africa

**Socioeconomic impact of HIV/AIDS · Research portfolio edition**  
**Blessing Sekeramavi | Original thesis: 20 May 2025**

## 1. Introduction
HIV/AIDS presents a long-term development challenge through its associations with health, human capital and economic activity. This project revisits the author’s completed master’s thesis as an accessible, reproducible research product. Its aim is to let readers inspect the evidence themselves and understand how country trajectories and model specifications affect the conclusions.

## 2. Objectives and research question
How are HIV prevalence, treatment coverage, education expenditure and economic development associated across Sub-Saharan Africa, and how do country trajectories differ?

## 3. Data sources and preparation
The embedded `Cleaned_Data_for_PowerBI` table contains **21,302 observations**, **48 countries**, **21 indicators**, and years **1990–2023**. Each row is a country–indicator–year observation. The table contains no missing Value cells and no duplicate country–indicator–year keys. This does **not** imply a balanced panel: many combinations are absent entirely. The recovery preserved numeric values and the original `Column1` row identifier; its historical meaning is unknown.

The original thesis identifies World Bank and UNAIDS sources. The recovered table includes World Bank indicator codes, but the original retrieval dates, API queries, and preprocessing scripts are unavailable. These are recovered dashboard values, not a newly downloaded or independently verified source release. Original interpolation described in the thesis cannot be reversed or independently verified from this extract.

## 4. Exploratory analysis and visual evidence
The overview compares five named countries without averaging percentages across countries. The Streamlit app enables all recovered countries, year filters, individual indicators, maps, matched country-year comparisons and CSV downloads. Countries with no observation in a selected map year remain absent. Different indicators retain their own units.

## 5. Methodology and recomputed results
The portfolio analysis uses complete cases for GDP growth, adult HIV prevalence and **adjusted savings: education expenditure (% of GNI)**. It fits pooled OLS and an OLS model with country indicator variables (country fixed effects), with standard errors clustered by country. No additional interpolation, outlier removal or forecasting is applied. The country fixed-effects specification includes no year effects. Its reported R² is the overall dummy-variable OLS R², not a within R². The model-wide clustered F statistic can be rank deficient because country dummies exceed independent cluster constraints; inference here is confined to the reported substantive coefficients.

| Model | Predictor | Coefficient | Clustered SE | p-value | N |
|---|---|---:|---:|---:|---:|
| Pooled OLS | hiv | -0.0380 | 0.0361 | 0.2919 | 1370 |
| Pooled OLS | education | -0.0257 | 0.0710 | 0.7170 | 1370 |
| Country fixed effects | hiv | -0.2212 | 0.1251 | 0.0770 | 1370 |
| Country fixed effects | education | 0.0811 | 0.0409 | 0.0476 | 1370 |

These estimates describe associations. Pooling and country fixed effects answer different questions; neither specification resolves reverse causality, time-varying confounding or selection from missing observations. The equations are deliberately documented rather than selected for statistical significance.

## 6. Discussion and comparison with the submitted thesis
The thesis's raw OLS output reports N = 853, R² = 0.010, HIV coefficient = −0.0825 and p = 0.003 (printed page 35). A separate fixed-effects results table reports an HIV coefficient of −1.65 and p = 0.234 (printed page 32). These are **historical thesis findings**, not reproduced results of this package. The original exact regression samples, transformations and full model data have not been recovered. The larger complete-case sample here does not reproduce the original model.

Several reconciliation issues should be resolved before claiming an exact replication:

- The thesis title specifies 1990–2023, the methods section states 2000–2023, and several chart headings extend to 2024. The recovered dashboard ends in 2023.
- Chapter 4 describes a four-component, equally weighted, normalized resilience index. Later text also describes an index based on GDP per capita growth minus HIV prevalence, and some case studies use a 0–10 scale. This package does not fabricate a single authoritative index from these inconsistent definitions.
- The recovered attainment indicator covers at least short-cycle tertiary education; it is not synonymous with bachelor's attainment. Education expenditure is also a different construct from education attainment.
- The recovered remittance variables are current US-dollar amounts, not remittances as a percentage of GDP. Population is available, but total GDP in current US dollars is not in this table. The required denominator for remittance/GDP ratios cannot be inferred from GDP growth.
- The summary OLS table's intercept standard error differs from the raw printed output. Refer to the raw output for historical reporting and to generated outputs for this reproduction.

## 7. Limitations and next steps
The source extract is not sufficient to recover the entire thesis workflow. Uneven coverage, possible inherited interpolation, alternative variable definitions and unobserved country-year shocks limit inference. Treat the models as exploratory and descriptive. Country-clustered errors allow within-country dependence, but do not repair omitted variables or identify causal effects.

Future work should recover the original scripts, freeze upstream data releases, reconcile resilience-index definitions and examine year effects, lagged treatment coverage, missingness sensitivity and alternative standard-error specifications. Recommendations about allocating health funding require additional causal and implementation evidence.

## 8. Reproducibility
Run `python scripts/analyze.py` from the repository after installing `requirements.txt`. This regenerates model summaries and coverage counts. Run `streamlit run app.py` to explore the recovered data. `data/provenance.json` identifies the recovery source and records its SHA-256 digest. `reports/recomputed_coefficients.csv` records the portfolio models reported above.

## 9. Conclusion
The recovered data supports a functioning dashboard and a transparent new analysis across 48 countries. The pooled model shows little explained variation, and the HIV coefficient changes when country effects are included. These results support careful attention to specification and national context rather than a single universal economic interpretation of HIV prevalence. They do not establish causal effects of treatment, education or HIV on growth.

The central contribution of this portfolio edition is a traceable path from recovered Power BI observations to interactive charts and documented model estimates. Exact replication of the original thesis, including its resilience index, remains dependent on recovering and reconciling the original analytic workflow.

## References and source materials
- Sekeramavi, B. (2025). *Resilience and Development in Sub-Saharan Africa: Analyzing the Socioeconomic Impact of HIV/AIDS (1990–2023).* Master's thesis, Constructor University. Supplied PDF, with printed-page references above.
- Author-supplied Power BI dashboard, `powerbi/Thesis_Dashboard.pbix`, table `Cleaned_Data_for_PowerBI`.
- World Bank and UNAIDS: original data providers named in the thesis; exact upstream releases not recovered.
- [Microsoft Power BI publishing documentation](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-publish-to-web).
- [Streamlit Community Cloud deployment documentation](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy).
