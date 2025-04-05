import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ---------- STREAMLIT CONFIG ----------
st.set_page_config(page_title="NEUROWEAVE Cost Comparison", layout="wide")
st.title("💸 NEUROWEAVE vs Traditional Valve: Cost Comparison")
st.markdown("### Scientific and Economic Visual Dashboard")

# ---------- DATA SIMULATION ----------
np.random.seed(42)
cost_data = pd.DataFrame({
    "Treatment": ["NEUROWEAVE", "Traditional Valve"] * 100,
    "Cost": np.concatenate([
        np.random.normal(12000, 500, 100),         # NEUROWEAVE
        np.random.normal(40000, 3000, 100)         # Valve
    ])
})

# ---------- 1. RADAR CHART ----------
categories = ['Initial', 'Maintenance', 'Surgery', 'Rehospitalization', 'Total']
neuro_vals = [12000, 0, 0, 0, 12000]
valve_vals = [10000, 10000, 10000, 10000, 40000]

radar = go.Figure()
radar.add_trace(go.Scatterpolar(r=neuro_vals, theta=categories, fill='toself', name='NEUROWEAVE', line_color='deepskyblue'))
radar.add_trace(go.Scatterpolar(r=valve_vals, theta=categories, fill='toself', name='Traditional Valve', line_color='crimson'))
radar.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
st.subheader("📌 Total Cost Breakdown (Radar Chart)")
st.plotly_chart(radar, use_container_width=True)

# ---------- 2. VIOLIN + BOXPLOT ----------
st.subheader("🎻 Distribution of Costs (Violin + Box)")
violin = px.violin(cost_data, y="Cost", x="Treatment", box=True, points="all", color="Treatment")
st.plotly_chart(violin, use_container_width=True)

# ---------- 3. TREEMAP ----------
st.subheader("🌲 Cost Structure (Treemap Hierarchy)")
tree = pd.DataFrame({
    "labels": ["NEUROWEAVE", "Valve", "Initial", "Maintenance", "Surgery", "Rehospitalization"],
    "parents": ["", "", "Valve", "Valve", "Valve", "Valve"],
    "values": [12000, 40000, 10000, 10000, 10000, 10000]
})
treemap = px.treemap(tree, path=['parents', 'labels'], values='values', color='values')
st.plotly_chart(treemap, use_container_width=True)

# ---------- 4. BARCHART ANIMADO ----------
st.subheader("📈 Cost Over Time (2023-2027)")
timeline = pd.DataFrame({
    "Year": list(range(2023, 2028)) * 2,
    "Treatment": ["NEUROWEAVE"] * 5 + ["Valve"] * 5,
    "Cost": [12000]*5 + [40000, 41000, 42000, 43000, 44000]
})
bar = px.bar(timeline, x="Year", y="Cost", color="Treatment", animation_frame="Year", barmode="group")
st.plotly_chart(bar, use_container_width=True)

# ---------- 5. SANKEY DIAGRAM ----------
st.subheader("🔀 Cost Flow Structure (Sankey Diagram)")
sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["Total", "Initial", "Maintenance", "Surgery", "Rehospitalization"]
    ),
    link=dict(source=[0, 0, 0, 0], target=[1, 2, 3, 4], value=[10000, 10000, 10000, 10000])
)])
st.plotly_chart(sankey, use_container_width=True)

# ---------- 6. PROJECTION LINES ----------
st.subheader("📉 Projection of Cost Evolution (Line)")
trend = pd.DataFrame({
    "Year": list(range(2023, 2028)),
    "NEUROWEAVE": [12000]*5,
    "Valve": [40000, 41000, 42000, 43000, 44000]
})
line = px.line(trend, x="Year", y=["NEUROWEAVE", "Valve"], markers=True)
st.plotly_chart(line, use_container_width=True)

# ---------- FOOTER ----------
st.markdown("---")
st.success("All visualizations are estimates based on clinical reports and economic projections. Costs are shown in USD.")
st.markdown("<p style='text-align: center;'>Designed by Sonia Annette Echeverría Vera | Young Scientist | UNESCO-Al Fozan Candidate</p>", unsafe_allow_html=True)
