from pathlib import Path
from itertools import count
import textwrap
from design import CSS, BRAND, HERO, PALETTE
import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
import os
from powerbi_support import valid_embed_url

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title='ResilienceAfrica | Health & Development', page_icon='✚', layout='wide')
st.markdown(CSS, unsafe_allow_html=True)
px.defaults.color_discrete_sequence = PALETTE
@st.cache_data
def load():
    return pd.read_csv(ROOT / 'data/thesis_data.csv')
df = load()
dictionary = df[['Series Code','Series Name']].drop_duplicates().set_index('Series Code')['Series Name'].to_dict()
st.markdown(HERO, unsafe_allow_html=True)
with st.sidebar:
    st.markdown(BRAND, unsafe_allow_html=True)
    st.header('Explore the evidence')
    countries = sorted(df['Country Name'].unique())
    selected = st.multiselect('Countries', countries, default=[c for c in ['Botswana','South Africa','Zimbabwe','Rwanda','Tanzania'] if c in countries])
    years = st.slider('Years', int(df.Year.min()), int(df.Year.max()), (1990,2023))
    indicator = st.selectbox('Indicator', list(dictionary), index=list(dictionary).index('SH.DYN.AIDS.ZS'), format_func=dictionary.get)
    st.markdown('<div class="ra-side-note"><strong>Reading the evidence</strong>Each indicator retains its original units. Missing country-years remain missing.</div>', unsafe_allow_html=True)
if not selected:
    st.info('Select at least one country to explore.'); st.stop()
f = df[df['Country Name'].isin(selected) & df.Year.between(*years)].copy()
st.markdown('<div class="ra-section-label">YOUR RESEARCH LENS</div>', unsafe_allow_html=True)
a,b,c,d = st.columns(4)
a.metric('Countries selected', len(selected)); b.metric('Observations', f'{len(f):,}'); c.metric('Indicators', f['Series Code'].nunique()); d.metric('Year window', f'{years[0]}–{years[1]}')
methods,trend,maptab,compare,models,powerbi,data = st.tabs(['Project report','Trends','Africa map','Relationships','Model results','Power BI','Data & coverage'])
chart_ids = count()
def chart(fig):
    fig.update_layout(template='plotly_white', paper_bgcolor='#FFFFFF', plot_bgcolor='#FFFFFF',
        font=dict(family='Inter, system-ui, sans-serif', color='#48636D', size=11),
        margin=dict(l=24,r=24,t=66 if fig.layout.title.text else 30,b=28),
        legend=dict(title_text='',orientation='h',y=-.18,x=0,font=dict(size=10),tracegroupgap=4),
        hoverlabel=dict(bgcolor='#153F47',font_color='#F5FAF8',bordercolor='#153F47'),
        colorway=PALETTE, title=dict(font=dict(size=14,color='#214752'),x=.02),
        modebar=dict(bgcolor='rgba(255,255,255,.8)',color='#78928F',activecolor='#007F78'))
    if fig.layout.title.text:
        fig.update_layout(title_text='<br>'.join(textwrap.wrap(fig.layout.title.text,68)))
    fig.update_xaxes(gridcolor='#EDF2F3',linecolor='#DCE7E8',zerolinecolor='#DCE7E8',title_font_size=10)
    fig.update_yaxes(gridcolor='#EDF2F3',linecolor='#DCE7E8',zerolinecolor='#DCE7E8',title_font_size=10)
    country_colors={name:PALETTE[i%len(PALETTE)] for i,name in enumerate(sorted(df['Country Name'].unique()))}
    series_colors={'Prevalence of HIV, total (% of population ages 15-49)':'#DB735B','Antiretroviral therapy coverage (% of people living with HIV)':'#007F78'}
    short_names={'Prevalence of HIV, total (% of population ages 15-49)':'HIV prevalence (%)','Antiretroviral therapy coverage (% of people living with HIV)':'ART coverage (%)','GDP growth (annual %)':'GDP growth','GDP per capita growth (annual %)':'GDP per capita growth'}
    for trace in fig.data:
        if trace.type=='scatter':
            color=series_colors.get(trace.name,country_colors.get(trace.name))
            if color: trace.update(line_color=color,marker_color=color)
            trace.update(line_width=2.3,marker_size=5)
            if trace.name in short_names: trace.name=short_names[trace.name]
    for annotation in fig.layout.annotations or []:
        annotation.update(text=annotation.text.replace('Country Name=',''),font=dict(size=11,color='#48636D'))
    st.plotly_chart(fig, width='stretch', key=f'chart_{next(chart_ids)}',config={'displaylogo':False,'scrollZoom':False})
with trend:
    q=f[f['Series Code']==indicator]
    st.subheader(dictionary[indicator])
    if q.empty: st.info('No observations for this selection.')
    else: chart(px.line(q.sort_values('Year'),x='Year',y='Value',color='Country Name',markers=True, labels={'Value':dictionary[indicator]}))
    l,r=st.columns(2)
    for container,code in [(l,'SH.HIV.ARTC.ZS'),(r,'SP.DYN.LE00.IN')]:
        with container:
            q=f[f['Series Code']==code]
            chart(px.line(q.sort_values('Year'),x='Year',y='Value',color='Country Name',title=dictionary[code],labels={'Value':dictionary[code]}))
with maptab:
    st.caption('The map covers all recovered countries, independent of the country selector. Select an exact year; unavailable values remain absent.')
    mapyear=st.slider('Map year',years[0],years[1],years[1]) if years[0]!=years[1] else years[0]
    q=df[(df.Year==mapyear)&(df['Series Code']==indicator)]
    if q.empty: st.info('No observations in this year.')
    else:
        fig=px.choropleth(q,locations='Country Code',color='Value',hover_name='Country Name',scope='africa',color_continuous_scale='Teal',title=f'{dictionary[indicator]} · {mapyear}')
        fig.update_geos(bgcolor='rgba(0,0,0,0)'); chart(fig)
with compare:
    left,right=st.columns(2)
    x=left.selectbox('Horizontal indicator',list(dictionary),index=list(dictionary).index('SH.DYN.AIDS.ZS'),format_func=dictionary.get)
    y=right.selectbox('Vertical indicator',list(dictionary),index=list(dictionary).index('NY.GDP.MKTP.KD.ZG'),format_func=dictionary.get)
    if x==y: st.info('Choose two different indicators.')
    else:
        p=f.pivot(index=['Country Name','Country Code','Year'],columns='Series Code',values='Value').reset_index()
        if x not in p or y not in p: st.info('Selected indicators are unavailable.')
        else:
            q=p.dropna(subset=[x,y]);st.caption(f'{len(q):,} matched country-year pairs. Correlation describes association; it does not establish causality.')
            if len(q)>1:
                chart(px.scatter(q,x=x,y=y,color='Country Name',hover_data=['Year'],labels={x:dictionary[x],y:dictionary[y]}))
                corr=q[x].corr(q[y]); st.metric('Pooled Pearson correlation', f'{corr:.3f}' if pd.notna(corr) else 'Undefined')
            else: st.info('Not enough overlapping observations.')
with methods:
    st.markdown('<div class="ra-report-heading"><h3>The research, in perspective.</h3><span>RESEARCH REPORT / 01</span></div>', unsafe_allow_html=True)
    with st.expander('Visual overview · five country trajectories', expanded=False):
        st.image(str(ROOT/'reports/overview.png'), width='stretch')
    st.markdown((ROOT/'reports/REPORT.md').read_text())
    st.download_button('Download full project report',(ROOT/'reports/REPORT.md').read_bytes(),'ResilienceAfrica_Report.md','text/markdown')
with data:
    st.subheader('Coverage before conclusions')
    coverage=f.groupby(['Country Name','Series Name']).agg(observations=('Value','count'),first_year=('Year','min'),last_year=('Year','max')).reset_index()
    coverage['possible_years']=years[1]-years[0]+1
    st.dataframe(coverage,width='stretch',hide_index=True)
    st.download_button('Download selected observations',f.to_csv(index=False),'selected_observations.csv','text/csv')
    st.download_button('Download complete recovered dataset',(ROOT/'data/thesis_data.csv').read_bytes(),'thesis_data.csv','text/csv')
    st.dataframe(f.drop(columns='Column1'),width='stretch',hide_index=True)

with models:
    st.subheader('Recomputed model results')
    st.caption('Full recovered sample: these results are fixed and do not change with sidebar filters. Complete cases; country-clustered standard errors.')
    coeff=pd.read_csv(ROOT/'reports/recomputed_coefficients.csv')
    st.dataframe(coeff,width='stretch',hide_index=True)
    st.caption('The education variable is adjusted savings: education expenditure (% of GNI). These models do not exactly reproduce the submitted thesis.')
    q=coeff[coeff.term=='hiv']
    fig=px.scatter(q,x='coefficient',y='model',error_x=1.96*q.std_error_clustered,title='HIV coefficient with approximate 95% normal confidence intervals')
    fig.add_vline(x=0,line_dash='dash');chart(fig)
    for name in ['pooled_ols','country_fe']:
        with st.expander(name.replace('_',' ').title()+' · full output'):
            st.code((ROOT/f'reports/{name}.txt').read_text(),language='text')
with powerbi:
    st.subheader('Power BI companion')
    st.write('Explore the original report’s analytical views below, recreated with interactive charts using the same recovered table.')
    st.download_button('Download original Power BI report',(ROOT/'powerbi/Thesis_Dashboard.pbix').read_bytes(),'Thesis_Dashboard.pbix','application/octet-stream')
    view=st.radio('Original report view',['Country indicator trends','HIV vs ART coverage','GDP growth comparison','Country indicator lookup'],horizontal=True)
    if view=='Country indicator trends':
        q=f[f['Series Code']==indicator].sort_values('Year')
        if q.empty: st.info('No observations for the selected indicator and period.')
        else: chart(px.line(q,x='Year',y='Value',color='Country Name',markers=True,labels={'Value':dictionary[indicator]}))
    elif view=='HIV vs ART coverage':
        q=f[f['Series Code'].isin(['SH.DYN.AIDS.ZS','SH.HIV.ARTC.ZS'])].sort_values('Year')
        if q.empty: st.info('No HIV or ART observations for this period.')
        else:
            fig=px.line(q,x='Year',y='Value',color='Series Name',facet_col='Country Name',facet_col_wrap=3,markers=True,labels={'Value':'Percent'},height=max(400,280*((q['Country Name'].nunique()+2)//3)))
            chart(fig)
    elif view=='GDP growth comparison':
        q=f[f['Series Code'].isin(['NY.GDP.MKTP.KD.ZG','NY.GDP.PCAP.KD.ZG'])].sort_values('Year')
        if q.empty: st.info('No GDP observations for this selection.')
        else: chart(px.line(q,x='Year',y='Value',color='Country Name',line_dash='Series Name',markers=True,labels={'Value':'Annual growth (%)'}))
        st.caption('The original R script referenced wide-format fields absent from its supplied long table. This view explicitly selects the two GDP indicator codes from the recovered data.')
    else:
        country=st.selectbox('Look up a country',selected)
        q=f[(f['Country Name']==country)&(f['Series Code']==indicator)].sort_values('Year')
        if q.empty: st.info('No observations available for this lookup.')
        else:
            first,last=q.iloc[0],q.iloc[-1]
            st.write(f"{country}: {dictionary[indicator]}")
            st.metric(f"Latest available · {int(last.Year)}",f"{last.Value:,.3f}")
            if len(q)>1: st.write(f"Change from {int(first.Year)} to {int(last.Year)}: {last.Value-first.Value:+,.3f} in the indicator’s original units.")
            st.caption('Structured data lookup; this replaces the original Power BI Q&A box without pretending to be an AI chatbot.')
    with st.expander('Original Power BI embed'):
        st.write('The original file uses R visuals, which Microsoft does not support in public Publish to web reports. The recreated views above work independently of Power BI.')
        st.markdown('[Power BI publishing requirements](https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-publish-to-web)')
        url=os.environ.get('POWERBI_EMBED_URL','')
        if not url and (ROOT/'.streamlit/secrets.toml').exists():
            url=st.secrets.get('POWERBI_EMBED_URL','')
        elif not url:
            try: url=st.secrets.get('POWERBI_EMBED_URL','')
            except FileNotFoundError: pass
        if url:
            if valid_embed_url(url):
                components.iframe(url,height=760,scrolling=True)
                st.caption('Power BI controls its own filters and permissions. Sidebar filters apply only to the recreated Streamlit charts. Secure embeds may require Microsoft sign-in and an appropriate licence.')
            else: st.error('Configure a valid HTTPS app.powerbi.com/view?r=… or app.powerbi.com/reportEmbed?reportId=… URL.')
        else:
            st.info('No published Power BI embed URL has been configured. Download the original PBIX or use the working recreated views above.')

st.markdown('<div class="ra-footer"><span>✚ &nbsp; ResilienceAfrica · Population health & development</span><span>Research by Blessing Sekeramavi</span></div>', unsafe_allow_html=True)
