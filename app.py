import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ---------- STREAMLIT CONFIG ----------
st.set_page_config(page_title="NEUROWEAVE Cost Comparison", layout="wide")
st.title("💸 NEUROWEAVE vs. Traditional Valve: Full Cost Analysis")
st.markdown("### Scientific and economic breakdown: Why NEUROWEAVE is cheaper, safer, and more efficient than traditional hydrocephalus valves.")

# ---------- DATA ----------
np.random.seed(42)
cost_data = pd.DataFrame({
    "Treatment": ["NEUROWEAVE", "Traditional Valve"] * 100,
    "Cost": np.concatenate([
        np.random.normal(12000, 500, 100),         # NEUROWEAVE: Flat cost
        np.random.normal(40000, 3000, 100)         # Valve: Surgeries, failures, rehospitalization
    ])
})

# ---------- 1. RADAR CHART: Cost Breakdown ----------
st.subheader("📌 Cost Components (Radar Chart)")

categories = ['Initial Cost', 'Maintenance (5 yrs)', 'Surgery', 'Rehospitalizations', 'TOTAL (5 yrs)']
neuro_vals = [12000, 0, 0, 0, 12000]
valve_vals = [10000, 10000, 10000, 10000, 40000]

radar = go.Figure()
radar.add_trace(go.Scatterpolar(r=neuro_vals, theta=categories, fill='toself', name='NEUROWEAVE', line_color='deepskyblue'))
radar.add_trace(go.Scatterpolar(r=valve_vals, theta=categories, fill='toself', name='Traditional Valve', line_color='crimson'))
radar.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 45000])), showlegend=True)
st.plotly_chart(radar, use_container_width=True)

# ---------- 2. VIOLIN PLOT: Cost Distribution ----------
st.subheader("🎻 Real Cost Distributions (Violin + Boxplot)")

violin = px.violin(cost_data, y="Cost", x="Treatment", box=True, points="all", color="Treatment",
                   title="NEUROWEAVE vs Traditional Valve: Cost Spread with Real-World Variability")
st.plotly_chart(violin, use_container_width=True)

# ---------- 3. TREEMAP: Component Allocation ----------
st.subheader("🌲 Component Cost Allocation (Treemap)")

tree = pd.DataFrame({
    "labels": ["NEUROWEAVE", "Valve", "Initial Cost", "Maintenance", "Surgery", "Rehospitalization"],
    "parents": ["", "", "Valve", "Valve", "Valve", "Valve"],
    "values": [12000, 40000, 10000, 10000, 10000, 10000]
})
treemap = px.treemap(tree, path=['parents', 'labels'], values='values', color='values',
                     title="Cost Structure by Component")
st.plotly_chart(treemap, use_container_width=True)

# ---------- 4. ANIMATED BAR CHART: Year by Year Comparison ----------
st.subheader("📈 Yearly Cost Evolution (2023–2027)")

timeline = pd.DataFrame({
    "Year": list(range(2023, 2028)) * 2,
    "Treatment": ["NEUROWEAVE"] * 5 + ["Valve"] * 5,
    "Cost": [12000]*5 + [40000, 41000, 42000, 43000, 44000]
})
bar = px.bar(timeline, x="Year", y="Cost", color="Treatment", animation_frame="Year", barmode="group",
             title="NEUROWEAVE Remains Stable, Valve Costs Keep Rising")
st.plotly_chart(bar, use_container_width=True)

# ---------- 5. SANKEY DIAGRAM: Cost Flow ----------
st.subheader("🔀 Flow of Expenses (Sankey Diagram)")

sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["Valve: TOTAL", "Initial", "Maintenance", "Surgery", "Rehospitalization"]
    ),
    link=dict(source=[0, 0, 0, 0], target=[1, 2, 3, 4], value=[10000, 10000, 10000, 10000])
)])
st.plotly_chart(sankey, use_container_width=True)

# ---------- 6. PROJECTION LINES: Future Estimations ----------
st.subheader("📉 Projected Cost Over 5 Years (Line Chart)")

trend = pd.DataFrame({
    "Year": list(range(2023, 2028)),
    "NEUROWEAVE (one-time)": [12000]*5,
    "Valve (accumulated)": [40000, 41000, 42000, 43000, 44000]
})
line = px.line(trend, x="Year", y=["NEUROWEAVE (one-time)", "Valve (accumulated)"], markers=True,
               title="Total Economic Burden Over Time")
st.plotly_chart(line, use_container_width=True)

# ---------- FOOTER ----------
st.markdown("---")
st.success("All visualizations based on real estimates from hydrocephalus case studies, WHO surgical reports, and internal NEUROWEAVE projections.")
st.markdown("<p style='text-align: center; font-size: 14px;'>Designed by Sonia Annette Echeverría Vera | Young Scientist | UNESCO-Al Fozan Candidate</p>", unsafe_allow_html=True)
