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
    ["Executive Summary", "Market Analysis", "Facility & Process Engineering", "Technical & Operations", "Financial Projections", "BOM & Costing Analysis"]
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
    
    # Projected market growth based on FMCG sector youth demographic drivers
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
        
        dot.edge('A1', 'B1')
        dot.edge('B1', 'C1')
        dot.edge('C1', 'D1')
        dot.edge('D1', 'E1')
        dot.edge('E1', 'F1')
        dot.edge('F1', 'G1')
        dot.edge('G1', 'H1')
        st.graphviz_chart(dot, use_container_width=True)

        st.markdown("---")
        st.markdown("### 📖 Detailed Process Guide: The Science of the Crunch")
        st.image(
            "Extruded_Snack_Manufacturing_Process_Guide.png",
            caption="Step-by-Step Guide to Extruded Snack Manufacturing — All 4 Phases",
            use_container_width=True
        )

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
        st.plotly_chart(fig_layout, use_container_width=True)

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

# --- PAGE 5: FINANCIAL PROJECTIONS (ERROR-FREE LOGIC) ---
elif page == "Financial Projections":
    st.title("💰 Financial Projections & Feasibility")
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Total CAPEX: 12,000,000 EGP")
        # Actual values extracted from the feasibility document
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
        
        # INTERNAL PANDAS CALCULATION (Fixes Excel #DIV/0! and #REF! errors)
        y1_revenue = 22000000
        y1_direct_costs = 14500000
        y1_overhead = 2000000
        growth_rate = 1.15  # Projecting a conservative 15% annual growth

        financials = pd.DataFrame({
            "Year": ["Year 1", "Year 2", "Year 3"],
            "Gross Revenue": [y1_revenue, y1_revenue * growth_rate, y1_revenue * (growth_rate**2)],
            "Direct Costs": [y1_direct_costs, y1_direct_costs * growth_rate, y1_direct_costs * (growth_rate**2)],
            "Overhead": [y1_overhead, y1_overhead * 1.10, y1_overhead * (1.10**2)] # Overhead grows at 10%
        })
        # Calculate EBITDA dynamically without circular references
        financials["EBITDA"] = financials["Gross Revenue"] - financials["Direct Costs"] - financials["Overhead"]

        fig_bar = go.Figure(data=[
            go.Bar(name='Gross Revenue', x=financials['Year'], y=financials['Gross Revenue'], marker_color='#2ca02c'),
            go.Bar(name='Direct Costs', x=financials['Year'], y=financials['Direct Costs'], marker_color='#d62728'),
            go.Bar(name='EBITDA', x=financials['Year'], y=financials['EBITDA'], marker_color='#1f77b4')
        ])
        fig_bar.update_layout(barmode='group', title="Income & Cost Analysis")
        st.plotly_chart(fig_bar, use_container_width=True)
        st.caption("*Year 1 data based on official feasibility estimates. Year 2 & 3 project 15% revenue scaling.*")

# --- PAGE 6: BOM & COSTING ANALYSIS (SNACKS ONLY) ---
elif page == "BOM & Costing Analysis":
    st.title("🌽 Snacks Product — BOM & Costing Analysis")
    st.markdown("IntelFix Costed BOM — Comprehensive breakdown of raw materials, packaging, and total cost structure for the **Extruded Snacks** product per 1,000 kg (1 Ton) production run.")
    st.markdown("---")

    # ── RAW DATA ──────────────────────────────────────────────────────────────
    rm_data = pd.DataFrame({
        "Material":      ["Corn-Local", "Corn-Imported", "Oil", "Flavour", "Salt", "Other-Mat", "Starch", "Milk"],
        "Input_KG":      [414.92, 295.36, 216.75, 67.11, 4.24, 0.89, 0.67, 0.06],
        "Formula_Pct":   [0.41492, 0.29536, 0.21675, 0.06711, 0.00424, 0.00089, 0.00067, 0.00006],
        "Unit_Cost_USD": [0.22, 0.24, 1.10, 5.00, 0.15, 1.00, 0.40, 2.80],
        "Total_Cost_USD":[91.2824, 70.8864, 238.425, 335.55, 0.636, 0.89, 0.268, 0.168],
    })

    pkg_data = pd.DataFrame({
        "Material":      ["Cartons", "Wrapper", "Outer", "Tape", "Plastic Bags", "Ink", "Banner", "Shrink"],
        "Qty":           [1843.81, 79.99, 33.08, 3.54, 1.10, 0.44, 0.02, 0.01],
        "UOM":           ["Pieces", "KG", "Pieces", "Rolls", "Pieces", "KG/Liters", "Pieces", "KG"],
        "Unit_Cost_USD": [0.15, 2.50, 0.25, 0.50, 0.05, 8.00, 5.00, 2.00],
        "Total_Cost_USD":[276.5715, 199.975, 8.27, 1.77, 0.055, 3.52, 0.10, 0.02],
    })

    total_rm_cost    = rm_data["Total_Cost_USD"].sum()       # 737.2738
    total_pkg_cost   = pkg_data["Total_Cost_USD"].sum()      # 490.2815
    total_bom_cost   = total_rm_cost + total_pkg_cost        # 1227.5553
    rm_pct_of_total  = total_rm_cost  / total_bom_cost * 100
    pkg_pct_of_total = total_pkg_cost / total_bom_cost * 100
    cost_per_kg      = total_bom_cost / 1000

    # ── KPI STRIP ─────────────────────────────────────────────────────────────
    k1, k2, k3, k4 = st.columns(4)
    k1.metric("Total Raw Material Cost / Ton", f"${total_rm_cost:,.2f}", "per 1,000 kg run")
    k2.metric("Total Packaging Cost / Ton",    f"${total_pkg_cost:,.2f}", "per 1,000 kg run")
    k3.metric("Total BOM Cost / Ton",          f"${total_bom_cost:,.2f}", "RM + Packaging")
    k4.metric("Cost per KG Finished Product",  f"${cost_per_kg:.4f}", "USD/kg")
    st.markdown("---")

    # ── TABS ──────────────────────────────────────────────────────────────────
    t1, t2, t3, t4, t5 = st.tabs([
        "📋 Formulation & BOM",
        "💵 Raw Materials Cost",
        "📦 Packaging Cost",
        "📊 Cost Structure Analysis",
        "🔬 Deep-Dive Insights"
    ])

    # ── TAB 1 : FORMULATION ───────────────────────────────────────────────────
    with t1:
        st.subheader("Snacks Formulation — per 1,000 kg (1 Ton) Batch")
        col_a, col_b = st.columns([1.3, 1])

        with col_a:
            display_rm = rm_data[["Material", "Input_KG", "Formula_Pct"]].copy()
            display_rm.columns = ["Material", "Input Mass (KG)", "Formula %"]
            display_rm["Formula %"] = (display_rm["Formula %"] * 100).round(3).astype(str) + "%"
            st.dataframe(display_rm, use_container_width=True, hide_index=True)
            st.info("ℹ️ Total batch = 1,000 KG finished product. Corn (local + imported) constitutes **~71%** of the formulation by mass.")

        with col_b:
            fig_form = px.pie(
                rm_data, values="Input_KG", names="Material",
                title="Ingredient Composition by Mass (KG)",
                color_discrete_sequence=px.colors.qualitative.Set3,
                hole=0.35
            )
            fig_form.update_traces(textinfo="label+percent", pull=[0.05 if m in ["Oil","Flavour"] else 0 for m in rm_data["Material"]])
            fig_form.update_layout(legend=dict(orientation="h", y=-0.15))
            st.plotly_chart(fig_form, use_container_width=True)

        st.markdown("#### Formulation Waterfall — Ingredient Stack per Ton")
        fig_bar_form = px.bar(
            rm_data.sort_values("Input_KG", ascending=True),
            x="Input_KG", y="Material", orientation="h",
            color="Input_KG",
            color_continuous_scale="Blues",
            labels={"Input_KG": "Mass (KG)", "Material": ""},
            title="Ingredient Input Mass — Ranked (per 1,000 kg Batch)"
        )
        fig_bar_form.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_bar_form, use_container_width=True)

    # ── TAB 2 : RAW MATERIALS COST ────────────────────────────────────────────
    with t2:
        st.subheader("Raw Materials — Detailed Cost Breakdown")
        col_a, col_b = st.columns([1.3, 1])

        with col_a:
            display_rm_cost = rm_data[["Material", "Input_KG", "Unit_Cost_USD", "Total_Cost_USD"]].copy()
            display_rm_cost.columns = ["Material", "Input (KG)", "Unit Cost (USD/KG)", "Total Cost (USD)"]
            display_rm_cost["Cost Share %"] = (rm_data["Total_Cost_USD"] / total_rm_cost * 100).round(1).astype(str) + "%"
            st.dataframe(display_rm_cost, use_container_width=True, hide_index=True)
            st.success(f"**Total Raw Material Cost: ${total_rm_cost:,.4f} USD / Ton**  \n"
                       f"Flavour and Oil together account for **{((335.55+238.425)/total_rm_cost*100):.1f}%** of raw material spend — the two highest-cost inputs.")

        with col_b:
            fig_rm_cost = px.bar(
                rm_data.sort_values("Total_Cost_USD", ascending=False),
                x="Material", y="Total_Cost_USD",
                color="Total_Cost_USD",
                color_continuous_scale="Oranges",
                labels={"Total_Cost_USD": "Total Cost (USD)", "Material": ""},
                title="Raw Material Cost Ranking"
            )
            fig_rm_cost.update_layout(coloraxis_showscale=False)
            st.plotly_chart(fig_rm_cost, use_container_width=True)

        st.markdown("#### Cost Efficiency View — Cost per KG of Each Ingredient")
        rm_data["Cost_Per_KG_Contribution"] = rm_data["Total_Cost_USD"] / 1000
        fig_eff = px.scatter(
            rm_data,
            x="Unit_Cost_USD", y="Input_KG",
            size="Total_Cost_USD", color="Material",
            labels={"Unit_Cost_USD": "Unit Cost (USD/KG)", "Input_KG": "Quantity Used (KG)"},
            title="Unit Cost vs. Quantity Used — Bubble size = Total Spend",
            color_discrete_sequence=px.colors.qualitative.Bold
        )
        fig_eff.update_traces(marker=dict(opacity=0.8))
        st.plotly_chart(fig_eff, use_container_width=True)
        st.caption("High-volume, low-cost ingredients (Corn) sit top-left. High-cost, moderate-volume inputs (Flavour, Oil) drive the largest spend despite lower mass.")

    # ── TAB 3 : PACKAGING COST ────────────────────────────────────────────────
    with t3:
        st.subheader("Packaging Materials — Detailed Cost Breakdown")
        col_a, col_b = st.columns([1.3, 1])

        with col_a:
            display_pkg = pkg_data[["Material", "Qty", "UOM", "Unit_Cost_USD", "Total_Cost_USD"]].copy()
            display_pkg.columns = ["Material", "Quantity", "UOM", "Unit Cost (USD)", "Total Cost (USD)"]
            display_pkg["Cost Share %"] = (pkg_data["Total_Cost_USD"] / total_pkg_cost * 100).round(1).astype(str) + "%"
            st.dataframe(display_pkg, use_container_width=True, hide_index=True)
            st.info(f"**Total Packaging Cost: ${total_pkg_cost:,.4f} USD / Ton**  \n"
                    f"Cartons and Wrapper film together represent **{((276.5715+199.975)/total_pkg_cost*100):.1f}%** of total packaging spend.")

        with col_b:
            fig_pkg_pie = px.pie(
                pkg_data, values="Total_Cost_USD", names="Material",
                title="Packaging Cost Share",
                color_discrete_sequence=px.colors.qualitative.Pastel,
                hole=0.35
            )
            fig_pkg_pie.update_traces(textinfo="label+percent")
            fig_pkg_pie.update_layout(legend=dict(orientation="h", y=-0.15))
            st.plotly_chart(fig_pkg_pie, use_container_width=True)

        fig_pkg_bar = px.bar(
            pkg_data.sort_values("Total_Cost_USD", ascending=True),
            x="Total_Cost_USD", y="Material", orientation="h",
            color="Total_Cost_USD",
            color_continuous_scale="Greens",
            labels={"Total_Cost_USD": "Total Cost (USD)", "Material": ""},
            title="Packaging Cost — Ranked by Spend"
        )
        fig_pkg_bar.update_layout(coloraxis_showscale=False)
        st.plotly_chart(fig_pkg_bar, use_container_width=True)

    # ── TAB 4 : COST STRUCTURE ────────────────────────────────────────────────
    with t4:
        st.subheader("Total BOM Cost Structure — Snacks Product")

        col_a, col_b = st.columns(2)

        with col_a:
            summary_df = pd.DataFrame({
                "Cost Category": ["Raw Materials", "Packaging"],
                "Total Cost (USD)": [total_rm_cost, total_pkg_cost],
                "% of BOM": [rm_pct_of_total, pkg_pct_of_total]
            })
            fig_summary_pie = px.pie(
                summary_df, values="Total Cost (USD)", names="Cost Category",
                title=f"RM vs Packaging Split (Total BOM = ${total_bom_cost:,.2f})",
                color_discrete_sequence=["#1f77b4", "#ff7f0e"],
                hole=0.4
            )
            fig_summary_pie.update_traces(textinfo="label+percent+value",
                                          texttemplate="%{label}<br>$%{value:,.2f}<br>(%{percent})")
            st.plotly_chart(fig_summary_pie, use_container_width=True)

        with col_b:
            # Combined top-10 spend drivers across RM + Packaging
            rm_combined = rm_data[["Material", "Total_Cost_USD"]].copy()
            rm_combined["Category"] = "Raw Material"
            pkg_combined = pkg_data[["Material", "Total_Cost_USD"]].copy()
            pkg_combined["Category"] = "Packaging"
            all_costs = pd.concat([rm_combined, pkg_combined]).sort_values("Total_Cost_USD", ascending=False).head(10)

            fig_top10 = px.bar(
                all_costs, x="Total_Cost_USD", y="Material", orientation="h",
                color="Category",
                color_discrete_map={"Raw Material": "#1f77b4", "Packaging": "#ff7f0e"},
                labels={"Total_Cost_USD": "Cost (USD)", "Material": ""},
                title="Top 10 Cost Drivers — RM + Packaging Combined"
            )
            fig_top10.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02))
            st.plotly_chart(fig_top10, use_container_width=True)

        st.markdown("---")
        st.markdown("#### Full Material Cost Waterfall — All Inputs Ranked")
        all_materials = pd.concat([rm_combined, pkg_combined]).sort_values("Total_Cost_USD", ascending=False).reset_index(drop=True)
        all_materials["Running Total"] = all_materials["Total_Cost_USD"].cumsum()
        fig_waterfall = go.Figure(go.Waterfall(
            name="Cost Build-Up", orientation="v",
            measure=["relative"] * len(all_materials) + ["total"],
            x=list(all_materials["Material"]) + ["TOTAL BOM"],
            y=list(all_materials["Total_Cost_USD"]) + [None],
            connector={"line": {"color": "rgb(63, 63, 63)"}},
            increasing={"marker": {"color": "#1f77b4"}},
            totals={"marker": {"color": "#2ca02c"}},
            text=[f"${v:,.2f}" for v in all_materials["Total_Cost_USD"]] + [f"${total_bom_cost:,.2f}"],
            textposition="outside"
        ))
        fig_waterfall.update_layout(
            title="BOM Cost Waterfall — Cumulative Spend Build-Up per Ton",
            height=420,
            yaxis_title="USD",
            showlegend=False
        )
        st.plotly_chart(fig_waterfall, use_container_width=True)

    # ── TAB 5 : DEEP-DIVE INSIGHTS ─────────────────────────────────────────────
    with t5:
        st.subheader("Strategic Insights & Cost Optimisation Opportunities")

        col_a, col_b = st.columns(2)

        with col_a:
            st.markdown("#### 🔴 Top Cost Concentration Risk")
            top3_rm = rm_data.nlargest(3, "Total_Cost_USD")
            top3_pct = top3_rm["Total_Cost_USD"].sum() / total_rm_cost * 100
            st.warning(
                f"**Flavour, Oil, and Corn-Local** account for **{top3_pct:.1f}%** of all raw material spend. "
                f"Supplier diversification and long-term contracts for these three ingredients are the highest-leverage "
                f"cost control actions available to management."
            )
            st.markdown("#### 📦 Packaging Efficiency")
            carton_pct = 276.5715 / total_pkg_cost * 100
            st.info(
                f"Carton boxes represent **{carton_pct:.1f}%** of packaging budget at 1,843 units per ton. "
                f"A carton right-sizing study (e.g. reducing count by 5% through higher packing density) "
                f"could yield **~${0.05 * carton_pct:.0f} USD/ton** in savings."
            )

        with col_b:
            st.markdown("#### 💡 Sensitivity: Flavour Price Scenarios")
            flavour_base = 5.00
            scenarios = pd.DataFrame({
                "Scenario": ["Best Case (−20%)", "Base Case", "Stress Case (+20%)", "Stress Case (+40%)"],
                "Flavour Unit Cost (USD/KG)": [4.00, 5.00, 6.00, 7.00],
                "Flavour Total Cost (USD)":   [67.11*4, 67.11*5, 67.11*6, 67.11*7],
            })
            scenarios["Total RM Cost (USD)"] = total_rm_cost - (67.11 * flavour_base) + scenarios["Flavour Total Cost (USD)"]
            scenarios["ΔvBase (USD)"] = scenarios["Total RM Cost (USD)"] - total_rm_cost

            fig_sens = px.bar(
                scenarios, x="Scenario", y="Total RM Cost (USD)",
                color="Scenario",
                color_discrete_sequence=["#2ca02c","#1f77b4","#ff7f0e","#d62728"],
                title="Flavour Price Sensitivity on Total RM Cost",
                text="Total RM Cost (USD)"
            )
            fig_sens.update_traces(texttemplate="$%{text:,.2f}", textposition="outside")
            fig_sens.update_layout(showlegend=False, yaxis_title="USD / Ton")
            st.plotly_chart(fig_sens, use_container_width=True)

        st.markdown("---")
        st.markdown("#### 📐 Cost Component Summary Table")
        summary_table = pd.DataFrame({
            "Component":       ["Corn (Local)", "Corn (Imported)", "Oil", "Flavour", "Salt + Other + Starch + Milk",
                                "Cartons", "Wrapper Film", "Outer + Tape + Other Pkg"],
            "USD / Ton":       [91.28, 70.89, 238.43, 335.55, 1.96,
                                276.57, 199.98, 13.73],
            "% of Total BOM":  [
                round(91.28  / total_bom_cost * 100, 1),
                round(70.89  / total_bom_cost * 100, 1),
                round(238.43 / total_bom_cost * 100, 1),
                round(335.55 / total_bom_cost * 100, 1),
                round(1.96   / total_bom_cost * 100, 1),
                round(276.57 / total_bom_cost * 100, 1),
                round(199.98 / total_bom_cost * 100, 1),
                round(13.73  / total_bom_cost * 100, 1),
            ],
            "Category": ["RM","RM","RM","RM","RM","Pkg","Pkg","Pkg"]
        })
        summary_table["% of Total BOM"] = summary_table["% of Total BOM"].astype(str) + "%"
        summary_table["USD / Ton"] = summary_table["USD / Ton"].apply(lambda x: f"${x:,.2f}")
        st.dataframe(summary_table, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.markdown(
            f"**📌 Bottom Line:** Total manufactured cost (materials + packaging) per ton of Snacks product is **${total_bom_cost:,.2f} USD**  "
            f"(equivalent to **${cost_per_kg:.4f} USD/kg**). At 150 kg/hr and 16-hour operational shifts, "
            f"the daily material cost exposure is approximately **${cost_per_kg * 150 * 16:,.0f} USD/day**, "
            f"underscoring the importance of bulk purchasing contracts for Flavour and Oil."
        )

    
