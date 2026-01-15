import requests
import re

def github_discovery(domain, token):
    print("[*] GitHub leak discovery running...")
    headers = {"Authorization": f"token {token}"}
    query = f"{domain} password OR api_key OR secret"
    url = f"https://api.github.com/search/code?q={query}"

    assets = set()
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        for item in r.json().get("items", []):
            text_url = item["html_url"]
            assets.add(text_url)

    return [{"asset": a, "source": "github"} for a in assets]
