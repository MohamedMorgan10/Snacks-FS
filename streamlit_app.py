import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import graphviz

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Sadat City Snack Plant",
    page_icon="🏭",
    layout="wide"
)

# --- SIDEBAR ---
st.sidebar.title("🏭 Feasibility Dashboard")
page = st.sidebar.radio("Navigation", [
    "Executive Summary",
    "Market Analysis",
    "Facility & Process Engineering",
    "Technical & Operations",
    "Financial Projections",
    "Risk Analysis"
])

# ==============================
# PAGE 1: EXECUTIVE SUMMARY
# ==============================
if page == "Executive Summary":
    st.title("🏭 Sadat City Extruded Snack Plant")

    col1, col2 = st.columns(2)

    col1.markdown("""
    ### 📌 Project Parameters
    - Location: Sadat City, Egypt  
    - Capacity: 150 kg/hr  
    - Technology: Twin-Screw Extrusion  
    - Packaging: 2 VFFS lines  
    """)

    col2.markdown("""
    ### 🎯 Strategic Goals
    - Break-even: Month 14  
    - OEE Target: 80%  
    - ROI: 2.5 – 3 years  
    """)

    st.success("✅ Project is financially viable and ready for execution.")

# ==============================
# PAGE 2: MARKET ANALYSIS
# ==============================
elif page == "Market Analysis":
    st.title("📊 Market Growth")

    data = pd.DataFrame({
        "Year": [2024, 2025, 2026, 2027, 2028],
        "Market": [12.5, 14.1, 16.0, 18.2, 20.5]
    })

    fig = px.line(data, x="Year", y="Market", markers=True)
    st.plotly_chart(fig, use_container_width=True)

# ==============================
# PAGE 3: FACILITY
# ==============================
elif page == "Facility & Process Engineering":
    st.title("📐 Process Flow")

    dot = graphviz.Digraph()
    dot.attr(rankdir='LR')

    dot.edges([
        ('Raw Material', 'Mixing'),
        ('Mixing', 'Extrusion'),
        ('Extrusion', 'Drying'),
        ('Drying', 'Coating'),
        ('Coating', 'Cooling'),
        ('Cooling', 'Packaging'),
        ('Packaging', 'Finished Goods')
    ])

    st.graphviz_chart(dot)

# ==============================
# PAGE 4: TECHNICAL
# ==============================
elif page == "Technical & Operations":
    st.title("⚙️ Operations")

    st.info("Power: 65 kW | Gas: 8 m³/hr | Air: 0.8 m³/min")

    st.markdown("""
    ✅ Lean Manufacturing  
    ✅ TPM  
    ✅ Predictive Maintenance  
    """)

# ==============================
# PAGE 5: FINANCIAL MODEL
# ==============================
elif page == "Financial Projections":
    st.title("💰 Financial Model")

    # --- USER INPUTS ---
    growth_rate = st.slider("Revenue Growth %", 5, 30, 15) / 100
    cost_ratio = st.slider("Direct Cost % of Revenue", 40, 80, 66) / 100
    overhead_growth = st.slider("Overhead Growth %", 5, 20, 10) / 100

    revenue_y1 = 22_000_000
    overhead_y1 = 2_000_000

    years = ["Year 1", "Year 2", "Year 3"]

    revenue = [
        revenue_y1,
        revenue_y1 * (1 + growth_rate),
        revenue_y1 * (1 + growth_rate)**2
    ]

    costs = [r * cost_ratio for r in revenue]

    overhead = [
        overhead_y1,
        overhead_y1 * (1 + overhead_growth),
        overhead_y1 * (1 + overhead_growth)**2
    ]

    df = pd.DataFrame({
        "Year": years,
        "Revenue": revenue,
        "Costs": costs,
        "Overhead": overhead
    })

    df["EBITDA"] = df["Revenue"] - df["Costs"] - df["Overhead"]

    # --- KPI SECTION ---
    col1, col2, col3 = st.columns(3)

    col1.metric("EBITDA Margin Y1", f"{df['EBITDA'][0] / df['Revenue'][0]:.1%}")
    col2.metric("EBITDA Year 3", f"{df['EBITDA'][2]:,.0f} EGP")
    col3.metric("Revenue Year 3", f"{df['Revenue'][2]:,.0f} EGP")

    # --- BAR CHART ---
    fig = go.Figure()
    fig.add_bar(name="Revenue", x=years, y=revenue)
    fig.add_bar(name="Costs", x=years, y=costs)
    fig.add_bar(name="EBITDA", x=years, y=df["EBITDA"])

    fig.update_layout(barmode="group")
    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # BREAK-EVEN ANALYSIS
    # =========================
    st.subheader("📉 Break-even Analysis")

    fixed_costs = overhead_y1
    contribution_margin = 1 - cost_ratio
    breakeven_revenue = fixed_costs / contribution_margin

    st.metric("Break-even Revenue", f"{breakeven_revenue:,.0f} EGP")

    # =========================
    # CASH FLOW
    # =========================
    st.subheader("💵 Cash Flow")


    
