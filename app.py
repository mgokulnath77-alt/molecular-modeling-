import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page Configuration ---
st.set_page_config(
    page_title="ArthroDock | COX-2 & Ibuprofen Lab",
    page_icon="🧬",
    layout="wide",
)

# --- Apple-Style Custom CSS ---
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #581c87 100%);
        color: white;
    }
    .stMetric {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    div[data-testid="stMetricValue"] {
        color: #22d3ee !important;
    }
    .step-box {
        padding: 10px 20px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_label_with_markdown=True)

# --- Sidebar ---
with st.sidebar:
    st.title("🧬 ARTHRO LAB")
    st.markdown("---")
    menu = st.radio("Navigation", ["Dashboard", "Molecular View", "Report Generator"])
    st.info("Team 3 | Bioinformatics Capstone 2026")

# --- Dashboard Content ---
if menu == "Dashboard":
    st.header("Computational Evaluation: Ibuprofen vs COX-2")
    st.write("Targeting Arthritis Inflammation via Molecular Docking Analysis")

    # Workflow Indicators
    cols = st.columns(5)
    steps = ["Start", "Upload", "Docking", "Analysis", "Report"]
    colors = ["#10b981", "#3b82f6", "#6366f1", "#8b5cf6", "#d1d5db"]
    for i, col in enumerate(cols):
        col.markdown(f"<div class='step-box' style='background:{colors[i]}'>{steps[i]}</div>", unsafe_allow_label_with_markdown=True)

    st.markdown("---")

    # Metrics Row
    m1, m2, m3 = st.columns(3)
    m1.metric("Binding Affinity", "-8.4 kcal/mol", delta="Optimal")
    m2.metric("H-Bonds", "3 Active", delta="Stable")
    m3.metric("Stability Score", "High", delta="92%")

    st.markdown("### Interaction Analysis Table")
    
    # Mock Data Table
    data = {
        "Residue": ["ARG-120", "TYR-355", "VAL-523", "GLY-526", "SER-530"],
        "Interaction Type": ["Hydrogen Bond", "van der Waals", "Hydrophobic", "Pi-Sigma", "Hydrogen Bond"],
        "Distance (Å)": [2.81, 3.42, 4.15, 3.88, 2.75],
        "Energy (kcal/mol)": [-1.2, -0.4, -0.2, -0.5, -1.1]
    }
    df = pd.DataFrame(data)
    st.table(df)

    # Visualization Simulation
    st.markdown("### Energy Distribution")
    fig = px.bar(df, x="Residue", y="Energy (kcal/mol)", color="Interaction Type", 
                 template="plotly_dark", title="Residue Energy Contribution")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Molecular View":
    st.subheader("3D Molecular Docking Viewer")
    st.warning("Note: Integrated NGL viewer requires a PDB file to render.")
    # Placeholder for NGL Viewer or 2D Diagram
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/62/Ibuprofen_docking_COX2.png", 
             caption="Example: Ibuprofen binding pocket interaction map (Discovery Studio Export)")

elif menu == "Report Generator":
    st.subheader("Final Project Report")
    st.text_area("Findings", value="The docking simulation of Ibuprofen against COX-2 reveals a strong binding affinity of -8.4 kcal/mol. The interaction is primarily stabilized by Hydrogen bonds with ARG-120 and SER-530...", height=200)
    if st.button("Generate PDF Report"):
        st.success("✅ Report 'COX2_Ibuprofen_Analysis.pdf' ready for download!")
