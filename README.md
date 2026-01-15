# 🛡️ PASSIVE-X

### Passive Attack Surface Discovery & Risk Scoring Platform

> **100% Passive | Zero Interaction | Enterprise-Grade OSINT Intelligence**

---

## 📌 Overview

**PASSIVE-X** is a **passive attack surface discovery and risk scoring platform** that identifies publicly exposed assets **without sending a single packet to the target infrastructure**.

Unlike traditional scanners, PASSIVE-X relies entirely on **open-source intelligence (OSINT)** and **publicly indexed data**, making it:

* ✅ Legally safe
* ✅ Silent (no detection by IDS/WAF)
* ✅ Ideal for pre-engagement, blue team visibility, and compliance audits

This project is designed as a **final-year cybersecurity project** with **real enterprise relevance**.

---

## 🎯 Problem Statement

Organizations often **do not know what they expose publicly**:

* Forgotten subdomains
* Old admin panels
* Leaked credentials
* Shadow or legacy assets

Active scanning:

* Is noisy
* Can be blocked
* Carries legal risk

---

## 💡 Solution

PASSIVE-X performs **100% passive reconnaissance** by aggregating and correlating multiple OSINT sources to:

* Discover assets
* Identify exposure
* Assign **risk scores**
* Generate **audit-ready reports**

> 🚫 No port scanning
> 🚫 No crawling
> 🚫 No interaction with target systems

---

## 🧠 Key Features

✔ Passive subdomain discovery
✔ Historical exposure analysis
✔ GitHub leak intelligence
✔ Shodan passive service visibility
✔ Google Dorking via search APIs
✔ Correlation-based risk scoring
✔ Web dashboard with dark SOC theme
✔ CSV & PDF report export

---

## 🔍 Passive Intelligence Sources

| Source                     | Purpose                       |
| -------------------------- | ----------------------------- |
| crt.sh                     | Certificate Transparency logs |
| Wayback Machine            | Historical URLs & endpoints   |
| GitHub Search              | Credential & secret leaks     |
| Shodan (API)               | Indexed services & banners    |
| Google Dorking (API-based) | Sensitive pages & files       |
| ASN / Metadata             | Shadow infrastructure         |

📌 **No scanning. No packets sent to the target.**

---

## 🏗️ Architecture

```
User (Web Dashboard)
        ↓
Passive OSINT Sources
        ↓
Correlation Engine
        ↓
Risk Scoring Engine
        ↓
Dashboard + Reports (CSV / PDF)
```

---

## 🖥️ Web Dashboard

The dashboard provides:

* 🎯 Domain input field
* 🔐 Optional API key inputs
* 🚀 One-click passive scan
* 📊 Risk-colored results table
* 📈 Summary metrics
* ⬇️ Download CSV & PDF buttons (appear after scan)

**Styled with a dark cybersecurity/SOC theme**

---

## ⚠️ Risk Scoring Model

Risk scores are calculated using:

```
Risk Score = Source Correlation + Asset Sensitivity + Exposure Type
```

### Severity Levels

| Score  | Severity |
| ------ | -------- |
| 80–100 | Critical |
| 55–79  | High     |
| 30–54  | Medium   |
| < 30   | Low      |

Assets appearing in **multiple sources** automatically receive higher risk.

---

## 📂 Project Structure

```
PASSIVE-X/
├── passivex.py          # CLI engine
├── dashboard.py         # Web dashboard
├── core/
│   ├── crtsh.py
│   ├── wayback.py
│   ├── github_leaks.py
│   ├── shodan_passive.py
│   ├── google_dorking.py
│   ├── correlate.py
│   └── risk.py
├── reports/
│   └── exporter.py
├── data/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/PASSIVE-X.git
cd PASSIVE-X
pip install -r requirements.txt
```

---

## ▶️ Usage

### 🔹 Run Web Dashboard

```bash
streamlit run dashboard.py
```

Open:

```
http://localhost:8501
```

### 🔹 Run CLI Version

```bash
python passivex.py -d example.com
```

With APIs:

```bash
python passivex.py -d example.com \
  --github-token YOUR_GITHUB_TOKEN \
  --shodan-key YOUR_SHODAN_KEY
```

---

## 📄 Output Reports

* `passivex_results.csv`
* `passivex_report.pdf`

Each report includes:

* Asset
* Intelligence sources
* Risk score
* Severity classification

---

## 🔐 Legal & Ethical Considerations

✔ Uses **publicly available data only**
✔ No active reconnaissance
✔ No traffic to target infrastructure
✔ Compliant with responsible disclosure principles

> This tool is designed for **defensive security, research, and education**.

---

## 👨‍💻 Author

**Pranav V**

---


Just tell me 👍
