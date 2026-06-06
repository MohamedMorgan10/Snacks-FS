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
    ["Executive Summary", "Market Analysis", "Facility & Process Engineering", 
     "Technical & Operations", "Financial Projections", "Snack Product Analysis"]
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
        * **Location:** Sadat City, Egypt (Industrial Zone)
        * **Core Product:** Puff Corn Extruded Snacks & Pellet Chips
        * **Capacity:** 150 kg/hr Base Line
        * **Primary Technology:** High-Precision Twin-Screw Extrusion
        * **Packaging:** 2x High-speed Vertical Form Fill Seal (VFFS) machines
        """)
    with col2:
        st.markdown("### 🎯 Strategic Objectives")
        st.markdown("""
        * Capture growing domestic demand for affordable, high-quality snacks.
        * Leverage competitive land pricing and industrial infrastructure in Sadat City.
        * Ensure maximum OEE (Overall Equipment Effectiveness) from Day 1.
        * Achieve ROI within the standard 3-year FMCG target window.
        """)
    st.info("💡 **Recommendation:** Proceed with CAPEX allocation for land acquisition and OEM down payments based on the positive 3-year financial outlook.")

# --- PAGE 2: MARKET ANALYSIS ---
elif page == "Market Analysis":
    st.title("📊 Market Analysis & Demand")
    st.markdown("---")
    market_data = pd.DataFrame({
        "Year": ["2024", "2025", "2026", "2027", "2028"],
        "Market Size (Billion EGP)": [12.5, 14.1, 16.0, 18.2, 20.5]
    })
    fig = px.bar(market_data, x="Year", y="Market Size (Billion EGP)", 
                 title="Projected Extruded Snack Market Size (Egypt)",
                 text_auto=True, color_discrete_sequence=["#1f77b4"])
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 3: FACILITY & PROCESS ENGINEERING ---
elif page == "Facility & Process Engineering":
    st.title("📐 Facility Layout & Process Flow")
    st.markdown("---")
    
    tab1, tab2 = st.tabs(["🔄 Processing Workflow", "🏗️ Facility Block Layout (Schematic)"])
    
    with tab1:
        st.markdown("### Technical Manufacturing Process Flow")
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='12,6')
        dot.attr('node', shape='box', fontname='Helvetica', fontsize='11')
        
        dot.node('A1', 'Bulk Intake\n(Corn Grits / Pellets)', style='filled', fillcolor='#D2E8F1')
        dot.node('A2', 'Sifting & De-stoning\n(Quality Gates)', style='filled', fillcolor='#D2E8F1')
        dot.node('B1', 'High-Speed Batch Mixing\n(Moisture Conditioning)', style='filled', fillcolor='#EAEAEA')
        dot.node('B2', 'Volumetric Feeding\n(Surge Hopper Control)', style='filled', fillcolor='#EAEAEA')
        dot.node('C1', 'Twin-Screw Extrusion\n(High Shear / Thermomechanical)', style='filled', fillcolor='#FBC4C4')
        dot.node('C2', 'Pneumatic Conveying\n(Venting & Transport)', style='filled', fillcolor='#FBC4C4')
        dot.node('D1', 'Continuous Multi-Pass\nDrying/Roasting Oven', style='filled', fillcolor='#FBC4C4')
        dot.node('E1', 'Slurry Preparation\n(Oil + Flavor Blending)', style='filled', fillcolor='#EAEAEA')
        dot.node('E2', 'Rotary Coating Drum\n(Liquid/Powder Application)', style='filled', fillcolor='#EAEAEA')
        dot.node('F1', 'Ambient Vibratory\nCooling Conveyor', style='filled', fillcolor='#EAEAEA')
        dot.node('G1', 'Multi-Head Weighers\n& 2x VFFS Systems', style='filled', fillcolor='#C1E9C1')
        dot.node('H1', 'Secondary Carton\nPacking & Coding', style='filled', fillcolor='#C1E9C1')
        dot.node('I1', 'Finished Goods\nPallet Storage', style='filled', fillcolor='#D2E8F1')
        
        dot.edges(['A1A2', 'A2B1', 'B1B2', 'B2C1', 'C1C2', 'C2D1', 'D1E2', 'E1E2', 'E2F1', 'F1G1', 'G1H1', 'H1I1'])
        
        st.graphviz_chart(dot, use_container_width=True)
        st.caption("*Process layout engineered to prevent cross-contamination.*")

    with tab2:
        st.markdown("### Plant Zoning & Master Layout")
        fig_layout = go.Figure()
        def add_zone(fig, x0, y0, x1, y1, color, name, description):
            fig.add_shape(type="rect", x0=x0, y0=y0, x1=x1, y1=y1, line=dict(color="black", width=2), fillcolor=color)
            fig.add_annotation(x=(x0+x1)/2, y=(y0+y1)/2, text=f"<b>{name}</b>", showarrow=False, font=dict(size=13, color="black"))
            fig.add_trace(go.Scatter(x=[(x0+x1)/2], y=[(y0+y1)/2], mode='markers', marker=dict(size=0.1, color='rgba(0,0,0,0)'), name=name, hoverinfo='text', text=f"<b>{name}</b><br>{description}"))

        fig_layout.add_shape(type="rect", x0=0, y0=0, x1=100, y1=100, line=dict(color="black", width=4))
        add_zone(fig_layout, 0, 75, 25, 100, "#a8d8ea", "Raw Material Intake", "Pneumatic unloading bays.")
        add_zone(fig_layout, 0, 0, 25, 75, "#aa96da", "Inventory & Warehouses", "Storage of materials.")
        add_zone(fig_layout, 25, 35, 75, 100, "#ffb6b9", "Main Production Hall", "Twin-screw extrusion processing.")
        add_zone(fig_layout, 75, 45, 100, 100, "#a8e6cf", "Finished Goods Warehouse", "Outbound dispatch.")
        add_zone(fig_layout, 25, 0, 45, 35, "#ffd3b6", "Maintenance Workshop", "Mechanical workshop.")
        add_zone(fig_layout, 45, 0, 60, 35, "#ffaaa5", "Quality Assurance Lab", "In-line sample analysis.")
        add_zone(fig_layout, 60, 0, 100, 45, "#d4f0f0", "Admin & Utilities", "Offices and control center.")
        
        fig_layout.update_layout(xaxis=dict(showgrid=False, visible=False, range=[-5, 105]), yaxis=dict(showgrid=False, visible=False, range=[-5, 105]), height=600, plot_bgcolor='white', showlegend=False)
        st.plotly_chart(fig_layout, use_container_width=True)

# --- PAGE 4: TECHNICAL & OPERATIONS ---
elif page == "Technical & Operations":
    st.title("⚙️ Technical Feasibility & Operations")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Equipment Specifications")
        st.success("**Extrusion Line**\n* 150 kg/hr Twin-Screw Extruder")
        st.info("**Packaging Cell**\n* 2 x VFFS Packaging Machines")
        st.warning("**Utility Consumptions**\n* ⚡ Electricity: ~65 kW/h\n* 🔥 Natural Gas: ~8 m³/hr\n* 💧 Water: ~25 L/hr\n* 💨 Compressed Air: ~0.8 m³/min")
    with col2:
        st.markdown("### Operational Excellence Framework")
        st.markdown("* **TPM:** Autonomous maintenance.\n* **Lean Manufacturing:** Continuous Gemba walks.\n* **Predictive Maintenance:** IntelFix system monitoring.")

# --- PAGE 5: FINANCIAL PROJECTIONS ---
elif page == "Financial Projections":
    st.title("💰 Financial Projections (3-Year Outlook)")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Estimated CAPEX Breakdown")
        capex_data = pd.DataFrame({"Category": ["Land", "Facility", "Extrusion", "Packaging", "Utilities"], "Cost Allocation (%)": [15, 25, 35, 15, 10]})
        fig_pie = px.pie(capex_data, values='Cost Allocation (%)', names='Category', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)
    with col2:
        st.markdown("### 3-Year P&L (EGP)")
        financials = pd.DataFrame({"Year": ["Year 1", "Year 2", "Year 3"], "Revenue": [45e6, 68e6, 95e6], "Operating Costs": [32e6, 41e6, 52e6], "Net Profit": [13e6, 27e6, 43e6]})
        fig_bar = go.Figure(data=[go.Bar(name='Revenue', x=financials['Year'], y=financials['Revenue'], marker_color='#2ca02c'), go.Bar(name='Operating Costs', x=financials['Year'], y=financials['Operating Costs'], marker_color='#d62728'), go.Bar(name='Net Profit', x=financials['Year'], y=financials['Net Profit'], marker_color='#1f77b4')])
        fig_bar.update_layout(barmode='group')
        st.plotly_chart(fig_bar, use_container_width=True)

# --- PAGE 6: SNACK PRODUCT ANALYSIS ---
elif page == "Snack Product Analysis":
    st.title("🍫 Snack Product Analysis")
    st.markdown("---")
    
    # Load Data
    try:
        file_path = "IntelFix_Costed_BOM_Formula.xlsx"
        df_form = pd.read_excel(file_path, sheet_name="Formulation (%)", header=1)
        df_raw = pd.read_excel(file_path, sheet_name="Raw Materials Cost", header=1)
        df_pack = pd.read_excel(file_path, sheet_name="Packaging Cost", header=1)
        
        tab1, tab2, tab3 = st.tabs(["📊 Formulation", "💰 Ingredient Costing", "🏭 Final Cost per Ton"])
        
        with tab1:
            st.subheader("Ingredient Composition (%)")
            st.dataframe(df_form[["Material Name", "Formula %"]].dropna(), use_container_width=True)
            fig_form = px.pie(df_form.dropna(), values='Formula %', names='Material Name', hole=0.4, title="Recipe Composition")
            st.plotly_chart(fig_form, use_container_width=True)
            
        with tab2:
            st.subheader("Ingredient & Packaging Cost Distribution")
            costs = pd.concat([df_raw[["Material Name", "Total Cost (USD)"]], df_pack[["Material Name", "Total Cost (USD)"]]])
            costs['Percentage'] = (costs['Total Cost (USD)'] / costs['Total Cost (USD)'].sum()) * 100
            st.dataframe(costs.style.format({"Total Cost (USD)": "${:.2f}", "Percentage": "{:.1f}%"}), use_container_width=True)
            fig_cost = px.bar(costs, x="Material Name", y="Total Cost (USD)", color="Material Name", title="Cost Breakdown per Batch")
            st.plotly_chart(fig_cost, use_container_width=True)

        with tab3:
            st.subheader("Final Product Costing (1 Ton Basis)")
            total_batch_cost = costs['Total Cost (USD)'].sum()
            metric_col1, metric_col2 = st.columns(2)
            metric_col1.metric("Total Batch Cost", f"${total_batch_cost:,.2f}")
            metric_col2.metric("Cost per Ton", f"${total_batch_cost:,.2f}")
            st.info("💡 Note: Data derived from current BOM and standard throughput rates.")
            
    except FileNotFoundError:
        st.error("Error: 'IntelFix_Costed_BOM_Formula.xlsx' not found. Please ensure the file is in the script directory.")
      
