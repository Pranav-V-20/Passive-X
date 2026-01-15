import requests

def crt_discovery(domain):
    print("[*] crt.sh discovery running...")
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    assets = set()

    try:
        r = requests.get(url, timeout=15)
        if r.status_code == 200:
            for entry in r.json():
                for sub in entry.get("name_value", "").split("\n"):
                    assets.add(sub.strip())
    except:
        pass

    return [{"asset": a, "source": "crt.sh"} for a in assets]
