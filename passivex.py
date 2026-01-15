import argparse
from core.crtsh import crt_discovery
from core.wayback import wayback_discovery
from core.github_leaks import github_discovery
from core.shodan_passive import shodan_discovery
from core.correlate import correlate_assets
from core.risk import score_assets
from reports.exporter import export_csv, export_pdf

def main():
    parser = argparse.ArgumentParser(
        description="PASSIVE-X | Passive Attack Surface Discovery & Risk Scoring"
    )
    parser.add_argument("-d", "--domain", required=True, help="Target domain")
    parser.add_argument("--github-token", help="GitHub Token (optional)")
    parser.add_argument("--shodan-key", help="Shodan API Key (optional)")
    args = parser.parse_args()

    print("[*] Starting passive reconnaissance...")

    assets = []
    assets += crt_discovery(args.domain)
    assets += wayback_discovery(args.domain)

    if args.github_token:
        assets += github_discovery(args.domain, args.github_token)

    if args.shodan_key:
        assets += shodan_discovery(args.domain, args.shodan_key)

    correlated = correlate_assets(assets)
    scored = score_assets(correlated)

    export_csv(scored)
    export_pdf(scored, args.domain)

    print("[+] Scan completed. Reports generated.")

if __name__ == "__main__":
    main()
