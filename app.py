import streamlit as st
import pandas as pd
import plotly.express as px

# --- 1. Page Config (Apple Style Setup) ---
st.set_page_config(
    page_title="ArthroDock | COX-2 & Ibuprofen Lab",
    page_icon="🧬",
    layout="wide",
)

# --- 2. Corrected CSS Styling (Fixed the TypeError) ---
st.markdown("""
    <style>
    /* Premium Dark Gradient Background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #581c87 100%);
        color: white;
    }
    
    /* Glassmorphism Cards for Metrics */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.07);
        padding: 20px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(12px);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }

    /* Style for the Progress Steps */
    .step-pill {
        padding: 8px 16px;
        border-radius: 50px;
        text-align: center;
        font-weight: 600;
        font-size: 0.9rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True) # FIXED: Changed from unsafe_allow_label... to unsafe_allow_html

# --- 3. Sidebar Navigation ---
with st.sidebar:
    st.title("🧬 ARTHRO LAB")
    st.markdown("---")
    menu = st.radio("Lab Navigation", ["Dashboard", "Docking Results", "Final Report"])
    st.info("Bioinformatics Capstone Project 2026")

# --- 4. Main Dashboard Page ---
if menu == "Dashboard":
    st.title("COX-2 Analyzer Dashboard")
    st.caption("Computational Evaluation: Ibuprofen Binding to Cyclooxygenase-2")

    # Workflow Stepper
    cols = st.columns(5)
    steps = ["Start", "Upload", "Docking", "Analysis", "Finish"]
    colors = ["#06b6d4", "#3b82f6", "#6366f1", "#8b5cf6", "#a855f7"]
    for i, col in enumerate(cols):
        col.markdown(f"<div class='step-pill' style='background:{colors[i]}'>{steps[i]}</div>", unsafe_allow_html=True)

    st.markdown("---")

    # Key Results Row
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("Binding Affinity", "-8.4 kcal/mol", "Optimal")
    with m2:
        st.metric("H-Bonds", "3 Active", "Stable")
    with m3:
        st.metric("Stability Score", "High", "94%")

    st.markdown("### Interaction Details")
    
    # Data Table
    data = {
        "Residue": ["ARG-120", "TYR-355", "VAL-523", "SER-530"],
        "Type": ["Hydrogen Bond", "van der Waals", "Hydrophobic", "Hydrogen Bond"],
        "Distance (Å)": [2.81, 3.42, 4.15, 2.75]
    }
    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)

    # Simple Chart
    st.markdown("### Energy Profile")
    fig = px.bar(df, x="Residue", y="Distance (Å)", color="Type", template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

elif menu == "Docking Results":
    st.subheader("Docking Visualization")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/62/Ibuprofen_docking_COX2.png", 
             caption="Visual comparison: Ibuprofen binding within the COX-2 active site pocket.")

elif menu == "Final Report":
    st.subheader("Report Summary")
    st.write("The evaluation confirms Ibuprofen's high therapeutic potential for arthritis through its stable binding at the ARG-120 junction.")
    st.button("Download PDF Report (Mock)")
