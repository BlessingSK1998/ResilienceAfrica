"""Visual identity for the ResilienceAfrica population-health observatory."""
PALETTE = ['#007F78', '#3174BB', '#DB735B', '#8B70AD', '#B08C38', '#4F8D9C', '#B85E83', '#626C83']
CSS = '''
<style>
:root { --ink:#16333F; --muted:#667D85; --teal:#007F78; --line:#DCE7E8; }
.stApp { background:#F4F8F8; }
[data-testid="stHeader"] { background:rgba(244,248,248,.94); }
.block-container { max-width:1550px; padding:2rem 3rem 4rem; }
html, body, [class*="st-"] { font-feature-settings:"ss01" on; }
h1,h2,h3 { color:var(--ink); letter-spacing:-.035em; }
p, li { line-height:1.75; }
[data-testid="stCaptionContainer"] { color:#657C85; }
a { color:#007F78; text-underline-offset:4px; }
[data-testid="stSidebar"] { background:#FFF; border-right:1px solid var(--line); }
[data-testid="stSidebar"]>div:first-child { padding-top:1.4rem; }
[data-testid="stSidebar"] h2 { font-size:1rem; letter-spacing:-.02em; margin-top:1.5rem; }
[data-testid="stSidebar"] label p { font-size:.76rem; font-weight:650; color:#526D76; }
[data-testid="stSidebar"] [data-baseweb="select"]>div { background:#F3F8F8; border:1px solid #E0EAEA; border-radius:12px; }
[data-baseweb="tag"] { background:#E0F0EC !important; color:#17635D !important; border-radius:7px; }
.ra-brand { display:flex; align-items:center; gap:11px; margin:0 0 2rem; }
.ra-symbol { display:grid; place-items:center; width:40px; height:40px; border-radius:12px; background:#007F78; box-shadow:0 5px 15px #007f7820; }
.ra-brand strong { font-size:17px; letter-spacing:-.5px; color:#173944; display:block; }
.ra-brand small { display:block; font-size:9px; font-weight:650; letter-spacing:1.7px; color:#738A90; margin-top:2px; }
.ra-side-kicker { color:#8A9FA5; font-size:10px; letter-spacing:2px; font-weight:700; padding-bottom:10px; border-bottom:1px solid #E6EEEE; }
.ra-side-note { border:1px solid #E0EBE9; background:#F4FAF8; border-radius:12px; padding:15px; color:#55756E; font-size:11px; line-height:1.7; margin-top:24px; }
.ra-side-note strong { display:block; color:#28746C; font-size:11px; margin-bottom:5px; }
.ra-topbar { display:flex; align-items:center; justify-content:space-between; margin:0 0 20px; gap:16px; }
.ra-breadcrumb { font-size:11px; color:#738991; letter-spacing:.3px; }
.ra-breadcrumb strong { color:#264C57; font-weight:600; }
.ra-status { font-size:10px; color:#3B6864; border:1px solid #D5E5DF; background:#EBF5F0; padding:6px 12px; border-radius:99px; white-space:nowrap; }
.ra-status i { width:5px; height:5px; background:#12816A; border-radius:50%; display:inline-block; margin-right:6px; vertical-align:middle; }
.ra-hero { position:relative; overflow:hidden; isolation:isolate; display:grid; grid-template-columns:1.3fr 1fr; background:#123A43; border:1px solid #254A52; border-radius:24px; min-height:318px; margin:0 0 14px; box-shadow:0 15px 40px #16333f0a; }
.ra-hero-copy { padding:35px 15px 32px 37px; z-index:1; }
.ra-eyebrow { display:flex; align-items:center; gap:9px; color:#ADDBCD; font-size:9px; letter-spacing:2.1px; font-weight:700; margin-bottom:17px; }
.ra-eyebrow svg { width:16px; height:16px; }
.ra-hero h1 { font-size:clamp(30px,3.1vw,49px); color:#F7FCFA; line-height:1.12; font-weight:650; margin:0 0 16px; letter-spacing:-1.7px; padding:0; }
.ra-hero h1 span { color:#9DE0CD; }
.ra-hero p { font-size:12px; color:#C2D6D8; line-height:1.85; max-width:395px; margin:0 0 23px; }
.ra-tags { display:flex; flex-wrap:wrap; gap:7px; }
.ra-tags span { border:1px solid #5E8F9355; color:#C0DCD8; padding:5px 9px; border-radius:7px; font-size:9px; letter-spacing:.2px; background:#ffffff05; }
.ra-hero-art { position:relative; display:flex; align-items:center; justify-content:center; background:radial-gradient(ellipse at 60% 40%,#27797555,transparent 70%); }
.ra-hero-art>svg { width:100%; max-width:400px; height:300px; }
.ra-hero-art::before { content:""; position:absolute; inset:0; background-image:radial-gradient(#8DBBB525 1px,transparent 1px); background-size:19px 19px; mask-image:linear-gradient(90deg,transparent,#000); }
.ra-credit { display:flex; justify-content:space-between; gap:15px; color:#6C858C; font-size:10px; margin:0 3px 23px; }
.ra-credit strong { font-weight:600; color:#3E616A; }
.ra-section-label { color:#6C858C; font-weight:650; letter-spacing:1.7px; font-size:9px; margin:0 0 11px; }
[data-testid="stMetric"] { position:relative; background:#FFF; padding:18px 21px; border-radius:15px; border:1px solid #DCE7E8; box-shadow:0 5px 16px #17394404; min-height:112px; }
[data-testid="stMetric"]::before { content:""; position:absolute; top:20px; right:20px; width:7px; height:7px; border-radius:50%; background:#B8DFD4; box-shadow:0 0 0 5px #F0F8F4; }
[data-testid="stMetricLabel"] p { font-size:10px; color:#738991; font-weight:600; letter-spacing:.25px; }
[data-testid="stMetricValue"] { font-size:29px; color:#214752; letter-spacing:-1.1px; font-weight:600; line-height:1.5; }
[data-testid="stTabs"] { margin-top:16px; }
[data-baseweb="tab-list"] { gap:5px; border-bottom:1px solid #DCE7E8; padding:0 0 8px; }
button[data-baseweb="tab"] { height:37px; padding:0 12px; background:transparent; border-radius:9px; color:#647F88; }
button[data-baseweb="tab"] p { font-size:11px; font-weight:550; }
button[data-baseweb="tab"][aria-selected="true"] { background:#E0EFEB; color:#076E64; }
[data-baseweb="tab-highlight"] { background:transparent; }
[data-baseweb="tab-panel"] { padding-top:24px; }
[data-testid="stPlotlyChart"] { border:1px solid #DFE9EA; background:#FFF; padding:7px 6px 1px; border-radius:16px; box-shadow:0 6px 20px #16333f04; overflow:hidden; }
[data-testid="stDataFrame"] { border:1px solid #DCE7E8; border-radius:13px; overflow:hidden; }
[data-testid="stExpander"] { border:1px solid #DCE7E8; background:#FFF; border-radius:12px; }
[data-testid="stDownloadButton"] button { border:1px solid #BBD4CE; border-radius:9px; background:#FFF; color:#166A61; font-size:11px; padding:9px 15px; transition:all .2s; }
[data-testid="stDownloadButton"] button:hover { background:#E9F5EF; border-color:#007F78; }
[data-testid="stRadio"] [role="radiogroup"] { gap:7px; }
[data-testid="stRadio"] label { border:1px solid #DCE7E8; background:#FFF; padding:5px 11px; border-radius:8px; }
[data-testid="stRadio"] label p { font-size:11px; }
[data-testid="stMarkdownContainer"] h1 { font-size:29px; line-height:1.3; max-width:820px; }
[data-testid="stMarkdownContainer"] h2 { font-size:20px; margin-top:26px; padding-bottom:10px; border-bottom:1px solid #DEE8E8; }
[data-testid="stMarkdownContainer"] h3 { font-size:18px; }
[data-testid="stMarkdownContainer"]>p, [data-testid="stMarkdownContainer"]>ul { font-size:13px; color:#48636D; }
[data-testid="stMarkdownContainer"] table { font-size:12px; border-radius:10px; overflow:hidden; }
[data-testid="stMarkdownContainer"] thead { background:#E7F1ED; color:#27584F; }
.ra-report-heading { display:flex; justify-content:space-between; align-items:center; margin-bottom:18px; }
.ra-report-heading h3 { margin:0; font-size:20px; color:#214752; letter-spacing:-.5px; }
.ra-report-heading>span { color:#789098; font-size:10px; }
.ra-footer { margin-top:45px; border-top:1px solid #DCE7E8; padding-top:17px; color:#7A9198; font-size:10px; display:flex; justify-content:space-between; gap:15px; }
@media(max-width:1000px) { .block-container{padding:1.6rem 1.4rem 3rem}.ra-hero-copy{padding:28px}.ra-hero{grid-template-columns:1.5fr 1fr}.ra-hero-art>svg{height:265px}.ra-hero h1{font-size:35px}.ra-hero p{font-size:11px} }
@media(max-width:640px) { .block-container{padding:1rem 1rem 2rem}.ra-hero{grid-template-columns:1fr;min-height:0}.ra-hero-copy{padding:26px}.ra-hero-art{display:none}.ra-hero h1{font-size:36px}.ra-topbar{align-items:flex-start}.ra-status{font-size:8px}.ra-credit{flex-direction:column;gap:3px}[data-testid="stMetric"]{padding:13px;min-height:90px}[data-testid="stMetricValue"]{font-size:22px}.ra-footer{flex-direction:column} }
@media(prefers-reduced-motion:reduce) { *{transition:none!important} }
/* Scope editorial styles so Streamlit's nested heading and metric markup retains hierarchy. */
[data-testid="stMarkdownContainer"] .ra-hero h1 { font-size:clamp(34px,3.4vw,49px); line-height:1.12; color:#F7FCFA; }
.ra-hero h1>span[data-heading-text] { color:#F7FCFA; }
.ra-hero h1>span[data-heading-text]>span { color:#9DE0CD; }
[data-testid="stMetricValue"] [data-testid="stMarkdownContainer"] p { font-size:29px; font-weight:600; color:#214752; line-height:1.5; letter-spacing:-1px; }
[data-testid="stMetricLabel"] [data-testid="stMarkdownContainer"] p { font-size:11px; color:#738991; }
[data-testid="stTabList"] { gap:5px; border-bottom:1px solid #DCE7E8; padding-bottom:8px; }
[data-testid="stTab"] { border-radius:9px; padding:9px 12px; color:#647F88; }
[data-testid="stTab"] [data-testid="stMarkdownContainer"] p { font-size:12px; font-weight:550; }
[data-testid="stTab"][aria-selected="true"] { background:#E0EFEB; color:#076E64; }
[data-testid="stTab"] .react-aria-SelectionIndicator { opacity:0; }
[data-testid="stTabPanel"] { padding-top:24px; }
[data-testid="stMarkdownContainer"] .ra-report-heading h3 { font-size:21px; margin:0; }
.ra-report-heading h3 [data-heading-text] { font-size:inherit; color:inherit; }
.ra-hero p { font-size:13px; }
.ra-eyebrow { font-size:10px; }
.ra-tags span { font-size:10px; }
.ra-credit { font-size:11px; }
.ra-status { font-size:11px; }
@media(max-width:640px) { [data-testid="stMarkdownContainer"] .ra-hero h1 { font-size:34px; } [data-testid="stMetricValue"] [data-testid="stMarkdownContainer"] p { font-size:23px; } }
</style>
'''
CROSS = '<svg width="23" height="23" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6V3Z" fill="#E7F8EF"/><path d="M9 12h2l1-3 1 6 1-3h2" stroke="#007F78" stroke-width="1.2" stroke-linejoin="round"/></svg>'
BRAND = '<div class="ra-brand"><div class="ra-symbol">'+CROSS+'</div><div><strong>ResilienceAfrica</strong><small>HEALTH & DEVELOPMENT</small></div></div><div class="ra-side-kicker">RESEARCH WORKSPACE</div>'
ART = '''<svg viewBox="0 0 400 300" role="img" aria-label="Decorative illustration of Africa and a population health pulse">
<defs><linearGradient id="af" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#8DDBC4" stop-opacity=".65"/><stop offset="1" stop-color="#398D88" stop-opacity=".2"/></linearGradient><linearGradient id="pulse"><stop stop-color="#96DCC8" stop-opacity="0"/><stop offset=".5" stop-color="#B7F3D9"/><stop offset="1" stop-color="#96DCC8" stop-opacity="0"/></linearGradient></defs>
<circle cx="212" cy="147" r="116" fill="none" stroke="#91CABB" stroke-opacity=".12"/><circle cx="212" cy="147" r="87" fill="none" stroke="#91CABB" stroke-opacity=".1" stroke-dasharray="3 6"/>
<path d="M158 53 186 48 209 58 231 60 244 80 265 89 274 110 298 115 282 137 263 151 258 180 244 195 236 223 220 250 209 256 201 239 190 214 185 186 173 169 156 170 145 155 125 154 112 137 108 115 117 96 131 89 137 67Z" fill="url(#af)" stroke="#A9E8D1" stroke-opacity=".55" stroke-width="1.2"/>
<path d="m280 200 9-15 3 18-9 23-7 7-1-14Z" fill="#73BCA7" fill-opacity=".4" stroke="#A9E8D1" stroke-opacity=".35"/>
<path d="M136 110 222 111 241 162 212 216 166 146 136 110 241 162 222 111 166 146 212 216" fill="none" stroke="#C4F4DF" stroke-opacity=".22" stroke-width=".8"/>
<g fill="#CAFFE5"><circle cx="136" cy="110" r="3"/><circle cx="222" cy="111" r="4"/><circle cx="166" cy="146" r="3"/><circle cx="241" cy="162" r="4"/><circle cx="212" cy="216" r="4"/></g>
<circle cx="212" cy="216" r="11" fill="none" stroke="#B5F1D3" stroke-opacity=".35"/><circle cx="241" cy="162" r="12" fill="none" stroke="#B5F1D3" stroke-opacity=".3"/>
<path d="M27 155h59l10-9 11 17 14-36 14 58 13-30h84l9-8 8 15 11-30 13 44 12-21h88" fill="none" stroke="url(#pulse)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="265" y="48" width="89" height="39" rx="10" fill="#234D54" stroke="#59867D" stroke-opacity=".45"/><path d="M279 60v13m-6-6h13" stroke="#A7E4CF" stroke-width="2"/><text x="294" y="65" font-family="sans-serif" font-size="7" fill="#D5EDE4" letter-spacing=".5">POPULATION</text><text x="294" y="76" font-family="sans-serif" font-size="7" fill="#D5EDE4" letter-spacing=".5">HEALTH</text>
<rect x="58" y="216" width="112" height="34" rx="9" fill="#234D54" stroke="#59867D" stroke-opacity=".4"/><circle cx="73" cy="233" r="3" fill="#A7E4CF"/><text x="84" y="236" font-family="sans-serif" font-size="8" fill="#D5EDE4">Evidence across Africa</text>
</svg>'''
HERO = '<div class="ra-topbar"><div class="ra-breadcrumb">Research observatory <span style="color:#BCCED1;padding:0 9px">/</span> <strong>Population health</strong></div><div class="ra-status"><i></i>RESEARCH PORTFOLIO · 2025</div></div><section class="ra-hero"><div class="ra-hero-copy"><div class="ra-eyebrow">'+CROSS+'HIV/AIDS & SOCIOECONOMIC DEVELOPMENT</div><h1>Health shocks.<br><span>Economic resilience.</span></h1><p>Explore the connections between treatment access, population health and development across Sub-Saharan Africa.</p><div class="ra-tags"><span>HIV & treatment</span><span>Population health</span><span>Economic resilience</span></div></div><div class="ra-hero-art">'+ART+'</div></section><div class="ra-credit"><span>Created by <strong>Blessing Sekeramavi</strong></span><span>Master’s thesis · Constructor University · 1990–2023</span></div>'
