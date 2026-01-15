def score_assets(assets):
    results = []

    for a in assets:
        score = 0
        sources = a["sources"]
        asset = a["asset"].lower()

        score += len(sources) * 20

        if "google_dork" in sources:
            score += 30

        if "shodan" in sources:
            score += 25

        if any(x in asset for x in ["admin", "login", "dashboard"]):
            score += 30

        if any(x in asset for x in ["dev", "test", "staging"]):
            score += 20

        score = min(score, 100)

        results.append({
            "asset": a["asset"],
            "sources": ", ".join(sources),
            "risk": score,
            "severity": severity(score)
        })

    return results

def severity(score):
    if score >= 80:
        return "Critical"
    if score >= 55:
        return "High"
    if score >= 30:
        return "Medium"
    return "Low"
