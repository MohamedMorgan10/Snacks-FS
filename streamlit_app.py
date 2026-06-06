import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import graphviz

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Investment Proposal: Sadat City Plant",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Presentation Menu")
st.sidebar.markdown("Navigate through the feasibility study sections:")
page = st.sidebar.radio("Go to", 
    ["Executive Summary", "Market Analysis", "Facility & Process Engineering", "Technical & Operations", "Financial Projections"]
)

# --- PAGE 1: EXECUTIVE SUMMARY ---
if page == "Executive Summary":
    st.title("🏭 Sadat City Extruded Snack Plant")
    st.subheader("Board of Directors Feasibility Presentation")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 📌 Project Parameters")
        st.markdown("""
        * **Location:** Sadat City, Monufia Governorate, Egypt
        * **Core Product:** Puff Corn Extruded Snacks 
        * **Capacity:** 150 kg/hr Base Line
        * **Primary Technology:** Jinan Sunward High-Precision Twin-Screw Extrusion
        * **Packaging:** 2x High-speed Vertical Form Fill Seal (VFFS) machines
        """)
    with col2:
        st.markdown("### 🎯 Strategic Objectives")
        st.markdown("""
        * Capture growing domestic demand for affordable, high-quality snacks.
        * Reach financial break-even point by month 14 of active production.
        * Ensure a steady 80% OEE (Overall Equipment Effectiveness) within the first 6 months.
        * Achieve Return on Investment (ROI) within 2.5 to 3 years.
        """)
    st.info("💡 **Recommendation:** The project is highly feasible. Proceed with the 12,000,000 EGP CAPEX allocation for land acquisition and machinery sourcing based on strong cash flow projections.")

# --- PAGE 2: MARKET ANALYSIS ---
elif page == "Market Analysis":
    st.title("📊 Market Analysis & Demand")
    st.markdown("---")
    
    market_data = pd.DataFrame({
        "Year": ["2024", "2025", "2026", "2027", "2028"],
        "Market Size (Billion EGP)": [12.5, 14.1, 16.0, 18.2, 20.5]
    })
    fig = px.line(market_data, x="Year", y="Market Size (Billion EGP)", 
                 title="Projected Extruded Snack Market Size Growth (Egypt)",
                 markers=True, text="Market Size (Billion EGP)")
    fig.update_traces(textposition="top center", line_color="#1f77b4", line_width=4, marker_size=10)
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 3: FACILITY & PROCESS ENGINEERING ---
elif page == "Facility & Process Engineering":
    st.title("📐 Facility Layout & Process Flow")
    st.markdown("---")
    
    tab1, tab2 = st.tabs(["🔄 Processing Workflow", "🏗️ Facility Block Layout (Schematic)"])
    
    # TAB 1: WORKFLOW (NATIVE PDF EXPORT)
    with tab1:
        st.markdown("### Technical Manufacturing Process Flow")
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='12,6')
        dot.attr('node', shape='box', fontname='Helvetica', fontsize='11')
        
        dot.node('A1', 'Bulk Intake\n(Corn Grits / 10-12% Moisture)', style='filled', fillcolor='#D2E8F1')
        dot.node('B1', 'Batch Mixing &\nConditioning (16-18% Target)', style='filled', fillcolor='#EAEAEA')
        dot.node('C1', 'Twin-Screw Extrusion\n(150 kg/hr / 130-180°C)', style='filled', fillcolor='#FBC4C4')
        dot.node('D1', 'Continuous\nDrying/Roasting Oven', style='filled', fillcolor='#FBC4C4')
        dot.node('E1', 'Rotary Coating Drum\n(Oil + Flavor Slurry)', style='filled', fillcolor='#EAEAEA')
        dot.node('F1', 'Ambient Vibratory\nCooling Conveyor', style='filled', fillcolor='#EAEAEA')
        dot.node('G1', 'Multi-Head Weighers\n& 2x VFFS Systems', style='filled', fillcolor='#C1E9C1')
        dot.node('H1', 'Finished Goods\nPalletizing', style='filled', fillcolor='#D2E8F1')
        
        dot.edges(['A1B1', 'B1C1', 'C1D1', 'D1E1', 'E1F1', 'F1G1', 'G1H1'])
        
        # Display Chart
        st.graphviz_chart(dot, use_container_width=True)
        
        # Native Graphviz PDF generation
        pdf_bytes_workflow = dot.pipe(format='pdf')
        st.download_button(
            label="📄 Download Workflow as PDF",
            data=pdf_bytes_workflow,
            file_name="Processing_Workflow_Sadat_Plant.pdf",
            mime="application/pdf"
        )

    # TAB 2: FACILITY LAYOUT (FIXED EXPORT - HTML)
    with tab2:
        st.markdown("### Plant Zoning & Master Layout")
        fig_layout = go.Figure()
        def add_zone(fig, x0, y0, x1, y1, color, name, description):
            fig.add_shape(type="rect", x0=x0, y0=y0, x1=x1, y1=y1, line=dict(color="black", width=2), fillcolor=color)
            fig.add_annotation(x=(x0+x1)/2, y=(y0+y1)/2, text=f"<b>{name}</b>", showarrow=False, font=dict(size=13, color="black"))
            fig.add_trace(go.Scatter(x=[(x0+x1)/2], y=[(y0+y1)/2], mode='markers', marker=dict(size=0.1, color='rgba(0,0,0,0)'), name=name, hoverinfo='text', text=f"<b>{name}</b><br>{description}"))

        fig_layout.add_shape(type="rect", x0=0, y0=0, x1=100, y1=100, line=dict(color="black", width=4))
        add_zone(fig_layout, 0, 75, 25, 100, "#a8d8ea", "RM Intake", "Pneumatic unloading bays.")
        add_zone(fig_layout, 0, 0, 25, 75, "#aa96da", "Inventory", "Climate controlled storage.")
        add_zone(fig_layout, 25, 35, 75, 100, "#ffb6b9", "Main Production Hall", "Extrusion and VFFS cells.")
        add_zone(fig_layout, 75, 45, 100, 100, "#a8e6cf", "Finished Goods", "Pallet racking & dispatch.")
        add_zone(fig_layout, 25, 0, 45, 35, "#ffd3b6", "Maintenance", "Workshop and spare parts.")
        add_zone(fig_layout, 45, 0, 60, 35, "#ffaaa5", "QA Lab", "In-line sampling.")
        add_zone(fig_layout, 60, 0, 100, 45, "#d4f0f0", "Admin", "Offices & control center.")

        fig_layout.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), height=550, margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='white', showlegend=False)
        
        # Display Chart
        st.plotly_chart(fig_layout, use_container_width=True)
        
        # --- THE FIX: Convert to HTML to bypass Kaleido crash ---
        html_bytes_layout = fig_layout.to_html(include_plotlyjs="cdn").encode("utf-8")
        st.download_button(
            label="🌐 Download Schematic Layout (HTML)",
            data=html_bytes_layout,
            file_name="Facility_Layout_Sadat_Plant.html",
            mime="text/html",
            help="Downloads an interactive webpage file so you don't lose the hover descriptions. If you absolutely need a PDF, open the downloaded HTML file and use Ctrl+P to Print to PDF."
        )

# --- PAGE 4: TECHNICAL & OPERATIONS ---
elif page == "Technical & Operations":
    st.title("⚙️ Technical Feasibility & Operations")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Equipment Specifications")
        st.success("**Extrusion Line**\n* 150 kg/hr Jinan Sunward Twin-Screw Extruder\n* Automated material feeding\n* High-efficiency continuous drying oven")
        st.info("**Packaging Cell**\n* 2 x VFFS Packaging Machines\n* Integrated multi-head weighers\n* Date coding and automated splicing")
        st.warning("**Utility Consumptions (Estimated Base Load)**\n* ⚡ **Electricity:** ~65 kW/h (Total Extrusion + Packaging)\n* 🔥 **Natural Gas:** ~8 m³/hr (Roasting/Drying Oven)\n* 💧 **Water:** ~25 L/hr (Conditioning & CIP requirements)\n* 💨 **Compressed Air:** ~0.8 m³/min @ 7 bar (Pneumatics & VFFS)")
        
    with col2:
        st.markdown("### Operational Excellence Framework")
        st.markdown("""
        * **Total Productive Maintenance (TPM):** Autonomous maintenance trained at the operator level.
        * **Lean Manufacturing:** Continuous Gemba walks and Root Cause Analysis (RCA) to mitigate waste.
        * **Predictive Maintenance:** Core assets integrated into centralized plant monitoring to prevent downtime.
        * **Labor & Compliance:** Standard 40-48 hour workweeks aligned with current 7,000 EGP private-sector minimum wage laws.
        """)

# --- PAGE 5: FINANCIAL PROJECTIONS ---
elif page == "Financial Projections":
    st.title("💰 Financial Projections & Feasibility")
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Total CAPEX: 12,000,000 EGP")
        capex_data = pd.DataFrame({
            "Asset Category": ["Land & Building", "Machinery & Installation", "Initial Working Capital"],
            "Amount (EGP)": [8000000, 2500000, 1500000]
        })
        fig_pie = px.pie(capex_data, values='Amount (EGP)', names='Asset Category', hole=0.4, 
                         color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c'])
        st.plotly_chart(fig_pie, use_container_width=True)
        st.caption("*Sourcing Structure: 60% Owner Equity, 40% Commercial Bank Loan (CBE Industrial Initiative).*")
        
    with col2:
        st.markdown("### 3-Year P&L Forecast (EGP)")
        
        y1_revenue = 22000000
        y1_direct_costs = 14500000
        y1_overhead = 2000000
        growth_rate = 1.15 

        financials = pd.DataFrame({
            "Year": ["Year 1", "Year 2", "Year 3"],
            "Gross Revenue": [y1_revenue, y1_revenue * growth_rate, y1_revenue * (growth_rate**2)],
            "Direct Costs": [y1_direct_costs, y1_direct_costs * growth_rate, y1_direct_costs * (growth_rate**2)],
            "Overhead": [y1_overhead, y1_overhead * 1.10, y1_overhead * (1.10**2)] 
        })
        financials["EBITDA"] = financials["Gross Revenue"] - financials["Direct Costs"] - financials["Overhead"]

        fig_bar = go.Figure(data=[
            go.Bar(name='Gross Revenue', x=financials['Year'], y=financials['Gross Revenue'], marker_color='#2ca02c'),
            go.Bar(name='Direct Costs', x=financials['Year'], y=financials['Direct Costs'], marker_color='#d62728'),
            go.Bar(name='EBITDA', x=financials['Year'], y=financials['EBITDA'], marker_color='#1f77b4')
        ])
        fig_bar.update_layout(barmode='group', title="Income & Cost Analysis")
        st.plotly_chart(fig_bar, use_container_width=True)
        st.caption("*Year 1 data based on official feasibility estimates. Year 2 & 3 project 15% revenue scaling.*")
