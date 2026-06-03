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
        * **Location:** Sadat City, Egypt (Industrial Zone)
        * **Core Product:** Puff Corn Extruded Snacks
        * **Capacity:** 150 kg/hr 
        * **Primary Technology:** Twin-screw extrusion line
        * **Packaging:** 2 High-speed Vertical Form Fill Seal (VFFS) machines
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

# --- PAGE 3: FACILITY & PROCESS ENGINEERING (NEW) ---
elif page == "Facility & Process Engineering":
    st.title("📐 Facility Layout & Process Flow")
    st.markdown("---")
    
    # Create two interactive tabs
    tab1, tab2 = st.tabs(["🔄 Processing Workflow", "🏗️ Facility Block Layout (Schematic)"])
    
    # TAB 1: WORKFLOW DIAGRAM
    with tab1:
        st.markdown("### Manufacturing Process Flow (150 kg/hr Puff Corn)")
        
        # Using Graphviz to create a professional flowchart
        dot = graphviz.Digraph()
        dot.attr(rankdir='LR', size='10,5')
        
        # Define nodes with colors
        dot.node('A', 'Raw Material Intake\n(Corn Grits, Oil, Flavors)', style='filled', fillcolor='#lightblue')
        dot.node('B', 'Mixing & Moisture\nConditioning', style='filled', fillcolor='#lightgrey')
        dot.node('C', 'Twin-Screw Extrusion\n(150 kg/hr)', style='filled', fillcolor='#ffcccb')
        dot.node('D', 'Drying / Roasting\nOven', style='filled', fillcolor='#ffcccb')
        dot.node('E', 'Flavoring Drum &\nSlurry Coating', style='filled', fillcolor='#lightgrey')
        dot.node('F', 'Cooling Conveyor', style='filled', fillcolor='#lightgrey')
        dot.node('G', '2x High-Speed\nVFFS Packaging', style='filled', fillcolor='#lightgreen')
        dot.node('H', 'Carton Packing &\nPalletizing', style='filled', fillcolor='#lightgreen')
        dot.node('I', 'Finished Goods\nInventory', style='filled', fillcolor='#lightblue')
        
        # Define edges
        dot.edges(['AB', 'BC', 'CD', 'DE', 'EF', 'FG', 'GH', 'HI'])
        
        st.graphviz_chart(dot, use_container_width=True)
        st.caption("*Process flow optimized for continuous operation and minimal changeover downtime.*")

    # TAB 2: FACILITY LAYOUT
    with tab2:
        st.markdown("### Plant Zoning & Master Layout")
        st.write("Conceptual footprint allocation based on Sadat City industrial zone standards. (Hover over zones for details).")
        
        # Using Plotly to draw a schematic block layout (AutoCAD proxy)
        fig_layout = go.Figure()

        # Helper function to add zones (rectangles)
        def add_zone(fig, x0, y0, x1, y1, color, name, description):
            fig.add_shape(type="rect", x0=x0, y0=y0, x1=x1, y1=y1, 
                          line=dict(color="black", width=2), fillcolor=color)
            # Add text annotation in the center of the shape
            fig.add_annotation(x=(x0+x1)/2, y=(y0+y1)/2, text=f"<b>{name}</b>", 
                               showarrow=False, font=dict(size=14, color="black"))
            # Add invisible scatter point for hover tooltip
            fig.add_trace(go.Scatter(x=[(x0+x1)/2], y=[(y0+y1)/2], mode='markers', 
                                     marker=dict(size=0.1, color='rgba(0,0,0,0)'),
                                     name=name, hoverinfo='text', 
                                     text=f"<b>{name}</b><br>{description}"))

        # Draw the main property boundary
        fig_layout.add_shape(type="rect", x0=0, y0=0, x1=100, y1=100, line=dict(color="black", width=4))

        # Add functional zones
        add_zone(fig_layout, 0, 60, 30, 100, "#a8d8ea", "Raw Material Intake", "Receiving bays, bulk silos, and initial inspection.")
        add_zone(fig_layout, 0, 0, 30, 60, "#aa96da", "RM Warehouse", "Climate-controlled storage for grits, oils, and flavoring powders.")
        add_zone(fig_layout, 30, 30, 70, 100, "#ffb6b9", "Main Production Hall", "Twin-screw extrusion, drying, flavoring, and 2x VFFS lines.")
        add_zone(fig_layout, 70, 40, 100, 100, "#a8e6cf", "Finished Goods", "Pallet racking, dispatch loading bays, and inventory control.")
        add_zone(fig_layout, 30, 0, 50, 30, "#ffd3b6", "Maintenance Workshop", "Tooling, spare parts, IntelFix terminal, and welding bays.")
        add_zone(fig_layout, 50, 0, 70, 30, "#ffaaa5", "Quality Lab", "In-line sampling, moisture testing, and QC compliance.")
        add_zone(fig_layout, 70, 0, 100, 40, "#d4f0f0", "Admin Building", "Offices, meeting rooms, staff changing rooms, and cafeteria.")

        # Update layout properties to look like a clean blueprint
        fig_layout.update_layout(
            xaxis=dict(showgrid=False, zeroline=False, visible=False, range=[-5, 105]),
            yaxis=dict(showgrid=False, zeroline=False, visible=False, range=[-5, 105]),
            height=600,
            margin=dict(l=20, r=20, t=20, b=20),
            plot_bgcolor='white',
            showlegend=False
        )
        
        st.plotly_chart(fig_layout, use_container_width=True)

# --- PAGE 4: TECHNICAL & OPERATIONS ---
elif page == "Technical & Operations":
    st.title("⚙️ Technical Feasibility & Operations")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Equipment Specifications")
        st.success("**Extrusion Line**\n* 150 kg/hr Twin-Screw Extruder\n* Automated material feeding\n* High-efficiency drying oven")
        st.info("**Packaging Cell**\n* 2 x VFFS Packaging Machines\n* Integrated multi-head weighers\n* Date coding and automated splicing")
    with col2:
        st.markdown("### Operational Excellence Framework")
        st.markdown("""
        * **Total Productive Maintenance (TPM):** Autonomous maintenance trained at the operator level.
        * **Lean Manufacturing:** Continuous Gemba walks and Root Cause Analysis (RCA).
        * **Predictive Maintenance:** Core assets integrated into the IntelFix system to prevent catastrophic downtime.
        """)

# --- PAGE 5: FINANCIAL PROJECTIONS ---
elif page == "Financial Projections":
    st.title("💰 Financial Projections (3-Year Outlook)")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Estimated CAPEX Breakdown")
        capex_data = pd.DataFrame({
            "Category": ["Land (Sadat City NUCA)", "Facility Construction", "Extrusion Line", "2x VFFS Packaging", "Utilities"],
            "Cost Allocation (%)": [15, 25, 35, 15, 10]
        })
        fig_pie = px.pie(capex_data, values='Cost Allocation (%)', names='Category', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with col2:
        st.markdown("### 3-Year P&L (EGP)")
        financials = pd.DataFrame({
            "Year": ["Year 1", "Year 2", "Year 3"],
            "Revenue": [45000000, 68000000, 95000000],
            "Operating Costs": [32000000, 41000000, 52000000],
            "Net Profit": [13000000, 27000000, 43000000]
        })
        fig_bar = go.Figure(data=[
            go.Bar(name='Revenue', x=financials['Year'], y=financials['Revenue'], marker_color='#2ca02c'),
            go.Bar(name='Operating Costs', x=financials['Year'], y=financials['Operating Costs'], marker_color='#d62728'),
            go.Bar(name='Net Profit', x=financials['Year'], y=financials['Net Profit'], marker_color='#1f77b4')
        ])
        fig_bar.update_layout(barmode='group')
        st.plotly_chart(fig_bar, use_container_width=True)