import streamlit as st
import pandas as pd
import os

from core.crtsh import crt_discovery
from core.wayback import wayback_discovery
from core.github_leaks import github_discovery
from core.shodan_passive import shodan_discovery
from core.google_dorking import google_dorking
from core.correlate import correlate_assets
from core.risk import score_assets
from reports.exporter import export_csv, export_pdf

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="PASSIVE-X Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: #ffffff;
}
.stButton>button {
    background-color: #00c2ff;
    color: black;
    border-radius: 8px;
    height: 45px;
    font-weight: bold;
}
.stTextInput>div>div>input {
    background-color: #1c1f26;
    color: white;
}
.risk-critical {color:#ff4b4b; font-weight:bold;}
.risk-high {color:#ffa500; font-weight:bold;}
.risk-medium {color:#ffd700; font-weight:bold;}
.risk-low {color:#00ff9c; font-weight:bold;}
</style>
""", unsafe_allow_html=True)

# -------------------- HEADER --------------------
st.title("🛡️ PASSIVE-X")
st.subheader("Passive Attack Surface Discovery & Risk Scoring Platform")
st.markdown("**100% Passive | Zero Legal Risk | Enterprise-Grade Intelligence**")
st.markdown("**Dev By Pranav V**")

st.divider()

# -------------------- INPUT PANEL --------------------
with st.form("scan_form"):
    domain = st.text_input("🎯 Target Domain", placeholder="example.com")
    github_token = st.text_input("🐙 GitHub Token (optional)", type="password")
    shodan_key = st.text_input("🌐 Shodan API Key (optional)", type="password")
    google_api = st.text_input("🔎 Google Dork API Key (SERP API)", type="password")


    submitted = st.form_submit_button("🚀 Run Passive Scan")

# -------------------- SCAN LOGIC --------------------
if submitted and domain:
    with st.spinner("Running passive reconnaissance..."):
        assets = []
        assets += crt_discovery(domain)
        assets += wayback_discovery(domain)

        if github_token:
            assets += github_discovery(domain, github_token)

        if shodan_key:
            assets += shodan_discovery(domain, shodan_key)

        if google_api:
            assets += google_dorking(domain, google_api)


        correlated = correlate_assets(assets)
        results = score_assets(correlated)

        df = pd.DataFrame(results)

        # Save reports
        export_csv(results)
        export_pdf(results, domain)

    st.success("✅ Scan completed successfully!")

    # -------------------- SUMMARY --------------------
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Assets", len(df))
    col2.metric("Critical", len(df[df["severity"] == "Critical"]))
    col3.metric("High", len(df[df["severity"] == "High"]))
    col4.metric("Medium", len(df[df["severity"] == "Medium"]))

    st.divider()

    # -------------------- RESULTS TABLE --------------------
    st.subheader("📊 Discovered Assets & Risk Scores")

    def style_severity(val):
        if val == "Critical":
            return "color:#ff4b4b;font-weight:bold"
        if val == "High":
            return "color:#ffa500;font-weight:bold"
        if val == "Medium":
            return "color:#ffd700;font-weight:bold"
        return "color:#00ff9c;font-weight:bold"

    styled_df = df.style.applymap(style_severity, subset=["severity"])
    st.dataframe(styled_df, use_container_width=True)

    st.divider()

    # -------------------- DOWNLOAD BUTTONS --------------------
    col1, col2 = st.columns(2)

    with col1:
        with open("passivex_results.csv", "rb") as f:
            st.download_button(
                "⬇️ Download CSV Report",
                f,
                file_name="passivex_results.csv",
                mime="text/csv"
            )

    with col2:
        with open("passivex_report.pdf", "rb") as f:
            st.download_button(
                "⬇️ Download PDF Report",
                f,
                file_name="passivex_report.pdf",
                mime="application/pdf"
            )

elif submitted:
    st.error("❌ Please enter a domain name.")
