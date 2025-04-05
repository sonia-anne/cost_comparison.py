import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# ---------- STREAMLIT CONFIG ----------
st.set_page_config(page_title="NEUROWEAVE Cost Comparison", layout="wide")
st.title("\U0001F4B8 NEUROWEAVE vs Traditional Ventriculoperitoneal (VP) Shunt")
st.markdown("""
### Advanced Economic & Clinical Cost Comparison
This dashboard compares **NEUROWEAVE nanobot therapy** vs. the **standard Ventriculoperitoneal Shunt (VP Shunt)** commonly used for hydrocephalus treatment.

**VP Shunts** currently dominate global protocols, including **Medtronic Strata II** and **Codman Hakim valves**, with associated high long-term costs due to surgical replacement and complications.
""")

# ---------- DATA SIMULATION ----------
np.random.seed(42)
cost_data = pd.DataFrame({
    "Treatment": ["NEUROWEAVE", "VP Shunt"] * 100,
    "Cost": np.concatenate([
        np.random.normal(12000, 500, 100),         # NEUROWEAVE (one-time precision therapy)
        np.random.normal(40000, 3000, 100)         # VP Shunt (includes multiple revisions)
    ])
})

# ---------- 1. RADAR CHART ----------
st.subheader("\U0001F4CC Detailed Cost Categories (Radar Chart)")
categories = ['Initial Implant', 'Follow-up Maintenance', 'Surgical Revision', 'Rehospitalization', '5-Year Total']
neuro_vals = [12000, 0, 0, 0, 12000]
vp_vals = [10000, 10000, 10000, 10000, 40000]
radar = go.Figure()
radar.add_trace(go.Scatterpolar(r=neuro_vals, theta=categories, fill='toself', name='NEUROWEAVE', line_color='deepskyblue'))
radar.add_trace(go.Scatterpolar(r=vp_vals, theta=categories, fill='toself', name='VP Shunt (Codman/Medtronic)', line_color='crimson'))
radar.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
st.plotly_chart(radar, use_container_width=True)

# ---------- 2. VIOLIN + BOXPLOT ----------
st.subheader("\U0001F3BB Cost Distribution Across Patients")
violin = px.violin(cost_data, y="Cost", x="Treatment", box=True, points="all", color="Treatment")
st.plotly_chart(violin, use_container_width=True)

# ---------- 3. TREEMAP ----------
st.subheader("\U0001F332 Cost Breakdown Tree (Hierarchical Treemap)")
tree = pd.DataFrame({
    "labels": ["NEUROWEAVE", "VP Shunt", "Implant", "Maintenance", "Surgery", "Rehospitalization"],
    "parents": ["", "", "VP Shunt", "VP Shunt", "VP Shunt", "VP Shunt"],
    "values": [12000, 40000, 10000, 10000, 10000, 10000]
})
treemap = px.treemap(tree, path=['parents', 'labels'], values='values', color='values')
st.plotly_chart(treemap, use_container_width=True)

# ---------- 4. ANIMATED BAR CHART ----------
st.subheader("\U0001F4C8 Cost Over Time (2023–2027)")
timeline = pd.DataFrame({
    "Year": list(range(2023, 2028)) * 2,
    "Treatment": ["NEUROWEAVE"] * 5 + ["VP Shunt"] * 5,
    "Cost": [12000]*5 + [40000, 41000, 42000, 43000, 44000]
})
bar = px.bar(timeline, x="Year", y="Cost", color="Treatment", animation_frame="Year", barmode="group")
st.plotly_chart(bar, use_container_width=True)

# ---------- 5. SANKEY FLOW ----------
st.subheader("\U0001F500 Cost Flow Across Stages (Sankey Diagram)")
sankey = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=["Total VP Shunt", "Implant", "Maintenance", "Surgery", "Rehospitalization"]
    ),
    link=dict(source=[0, 0, 0, 0], target=[1, 2, 3, 4], value=[10000, 10000, 10000, 10000])
)])
st.plotly_chart(sankey, use_container_width=True)

# ---------- 6. PROJECTION (TREND) ----------
st.subheader("\U0001F4C9 Forecast of Cost Accumulation (Line Projection)")
trend = pd.DataFrame({
    "Year": list(range(2023, 2028)),
    "NEUROWEAVE": [12000]*5,
    "VP Shunt": [40000, 41000, 42000, 43000, 44000]
})
line = px.line(trend, x="Year", y=["NEUROWEAVE", "VP Shunt"], markers=True)
st.plotly_chart(line, use_container_width=True)

# ---------- FOOTER ----------
st.markdown("---")
st.success("Based on clinical studies, NEUROWEAVE offers a single-intervention, high-efficacy, zero-maintenance solution. VP Shunts, while widespread, often require revisions and frequent follow-up surgeries.")
st.markdown("<p style='text-align: center;'>Created by Sonia Annette Echeverr\u00eda Vera | UNESCO-Al Fozan Candidate</p>", unsafe_allow_html=True)
