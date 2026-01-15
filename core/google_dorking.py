import requests

def google_dorking(domain, api_key):
    """
    Passive Google Dorking using SERP API
    """
    print("[*] Google Dorking (passive) running...")

    dorks = [
        f"site:{domain} intitle:admin",
        f"site:{domain} inurl:login",
        f"site:{domain} filetype:pdf",
        f"site:{domain} filetype:xls",
        f"site:{domain} \"confidential\"",
    ]

    assets = set()

    for dork in dorks:
        params = {
            "engine": "google",
            "q": dork,
            "api_key": api_key
        }

        r = requests.get("https://serpapi.com/search", params=params)
        if r.status_code == 200:
            for res in r.json().get("organic_results", []):
                assets.add(res.get("link"))

    return [{"asset": a, "source": "google_dork"} for a in assets]
