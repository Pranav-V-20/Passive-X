import requests

def shodan_discovery(domain, api_key):
    print("[*] Shodan passive discovery running...")
    url = "https://api.shodan.io/shodan/host/search"
    params = {
        "key": api_key,
        "query": f"hostname:{domain}"
    }

    assets = []

    r = requests.get(url, params=params)
    if r.status_code == 200:
        for match in r.json().get("matches", []):
            hostnames = match.get("hostnames", [])
            product = match.get("product", "unknown")
            port = match.get("port", "N/A")

            for host in hostnames:
                assets.append({
                    "asset": host,
                    "source": "shodan",
                    "meta": f"{product}:{port}"
                })

    return assets
