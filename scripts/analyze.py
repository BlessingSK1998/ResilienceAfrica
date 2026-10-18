"""Reproduce descriptive summaries and two explicitly specified association models."""
from pathlib import Path
import pandas as pd
import statsmodels.formula.api as smf
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/'data/thesis_data.csv')
p=df.pivot(index=['Country Code','Year'],columns='Series Code',values='Value').reset_index()
p=p.rename(columns={'Country Code':'country','NY.GDP.MKTP.KD.ZG':'gdp_growth','SH.DYN.AIDS.ZS':'hiv','NY.ADJ.AEDU.GN.ZS':'education'})
sample=p.dropna(subset=['gdp_growth','hiv','education'])
if sample.empty: raise ValueError('No overlapping model observations')
for name,formula in [('pooled_ols','gdp_growth ~ education + hiv'),('country_fe','gdp_growth ~ education + hiv + C(country)')]:
    model=smf.ols(formula,data=sample).fit(cov_type='cluster',cov_kwds={'groups':sample.country})
    (ROOT/f'reports/{name}.txt').write_text(str(model.summary()))
    print(name, 'N=',int(model.nobs),'R2=',model.rsquared,'HIV coefficient=',model.params.hiv)
df.groupby(['Series Code','Series Name']).agg(n=('Value','count'),countries=('Country Code','nunique'),first_year=('Year','min'),last_year=('Year','max')).to_csv(ROOT/'reports/coverage.csv')
