import requests

def wayback_discovery(domain):
    print("[*] Wayback discovery running...")
    url = f"http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json"
    assets = set()

    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            for row in r.json()[1:]:
                assets.add(row[2].split("/")[0])
    except:
        pass

    return [{"asset": a, "source": "wayback"} for a in assets]
