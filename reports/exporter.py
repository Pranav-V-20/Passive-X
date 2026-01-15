import pandas as pd
from fpdf import FPDF

def export_csv(data):
    df = pd.DataFrame(data)
    df.to_csv("passivex_results.csv", index=False)
    print("[+] CSV report generated")

def export_pdf(data, domain):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"PASSIVE-X Exposure Report: {domain}", ln=True)

    pdf.set_font("Arial", size=10)
    for d in data:
        pdf.multi_cell(0, 8,
            f"Asset: {d['asset']}\n"
            f"Sources: {d['sources']}\n"
            f"Risk: {d['risk']} ({d['severity']})\n"
            "-------------------------------------"
        )

    pdf.output("passivex_report.pdf")
    print("[+] PDF report generated")
