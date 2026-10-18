"""Validate embed URLs without fetching or storing authentication credentials."""
from urllib.parse import urlparse, parse_qs

def valid_embed_url(url):
    try:
        parsed=urlparse(url)
        params=parse_qs(parsed.query)
        return (parsed.scheme=='https' and parsed.netloc=='app.powerbi.com'
                and ((parsed.path=='/view' and bool(params.get('r')))
                     or (parsed.path=='/reportEmbed' and bool(params.get('reportId')))))
    except ValueError:
        return False
