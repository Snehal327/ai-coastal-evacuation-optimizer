import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Coastal Evacuation Optimizer",
    layout="wide"
)

st.title("AI-Powered Last-Mile Evacuation Optimization")

st.subheader("Coastal Maharashtra")

data = pd.read_csv("data/cyclone_data.csv")

st.metric(
    "Locations Analysed",
    len(data)
)

high_risk = len(
    data[data["wind_speed"] >= 120]
)

st.metric(
    "High Risk Locations",
    high_risk
)

st.subheader("Cyclone Risk Data")

st.dataframe(data)

st.subheader("Evacuation Status")

risk = st.selectbox(
    "Select Risk Level",
    ["LOW", "MEDIUM", "HIGH"]
)

if risk == "HIGH":
    st.error(
        "CRITICAL: Immediate evacuation recommended."
    )

elif risk == "MEDIUM":
    st.warning(
        "WARNING: Prepare for possible evacuation."
    )

else:
    st.success(
        "LOW RISK: Continue monitoring official updates."
    )
