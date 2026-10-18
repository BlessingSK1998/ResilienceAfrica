# Original Power BI support

The author-supplied PBIX is preserved as `Thesis_Dashboard.pbix`. Its table was recovered without new interpolation. `visual_manifest.json` records original page/visual/field mappings. The original R visual scripts are preserved for inspection.

## What works in Streamlit

- Original country indicator time series, recreated using Plotly.
- HIV prevalence vs ART coverage, faceted by country.
- GDP growth vs GDP per capita growth, corrected to use long-format indicator codes.
- Structured country/indicator lookup in place of Power BI Q&A.
- Interactive Africa choropleth in the Africa map tab.
- Original PBIX download, plus data and full project report downloads.

These are functioning recreations; they do not execute the Power BI engine or the original R runtime. Streamlit filters do not control a native Power BI iframe.

## Optional original report iframe

Publish an eligible report to the Power BI service and obtain its official iframe URL. Put the iframe `src` URL in Streamlit Community Cloud app settings → Secrets:

```toml
POWERBI_EMBED_URL = "PASTE_YOUR_ACTUAL_POWER_BI_IFRAME_SRC_URL"
```

The app accepts HTTPS `app.powerbi.com/view?r=…` or `app.powerbi.com/reportEmbed?reportId=…` links. Do not use the Teams landing page, a PBIX file URL or an entire iframe HTML tag. Never store passwords or embed tokens in the repository.

The original contains three R script visuals, which are unsupported by Publish to web. To publish a compatible native Power BI report, replace its R visuals with standard Power BI line charts and remove/replace any other unsupported visuals. See the Microsoft documentation below. A secure embed may require user sign-in, report permissions and appropriate licensing. This package has not verified a native embed because no published report URL is available.

Publish to web exposes the report and its underlying model publicly. Use it only for data intended to be public.

- https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-publish-to-web
- https://learn.microsoft.com/en-us/power-bi/collaborate-share/service-embed-secure
