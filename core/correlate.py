def correlate_assets(assets):
    correlated = {}

    for a in assets:
        asset = a["asset"]
        correlated.setdefault(asset, {
            "sources": set(),
            "meta": []
        })

        correlated[asset]["sources"].add(a["source"])
        if "meta" in a:
            correlated[asset]["meta"].append(a["meta"])

    results = []
    for asset, info in correlated.items():
        results.append({
            "asset": asset,
            "sources": list(info["sources"]),
            "meta": ", ".join(info["meta"])
        })

    return results
