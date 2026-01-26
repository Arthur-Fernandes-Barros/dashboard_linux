import streamlit as st
import psutil
import time
import pandas as pd
from datetime import datetime
import altair as alt

st.set_page_config(layout="wide")

st.title("Linux System Dashboard")

if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=["Hora", "CPU", "RAM", "Disco"])

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

col1, col2, col3 = st.columns(3)

col1.metric("CPU", f"{cpu}%")
col2.metric("RAM", f"{ram}%")
col3.metric("Disco", f"{disk}%")

new_row = {
    "Hora": datetime.now().strftime("%H:%M:%S"),
    "CPU": cpu,
    "RAM": ram,
    "Disco": disk,
}

st.session_state.data = pd.concat(
    [st.session_state.data, pd.DataFrame([new_row])],
    ignore_index=True,
).tail(50)

cpu_chart = (
    alt.Chart(st.session_state.data)
    .mark_line(color="#FF4B4B")
    .encode(x="Hora:N", y="CPU:Q", tooltip=["Hora", "CPU"])
    .properties(title="Uso de CPU (%)")
)

ram_chart = (
    alt.Chart(st.session_state.data)
    .mark_line(color="#4CAF50")
    .encode(x="Hora:N", y="RAM:Q", tooltip=["Hora", "RAM"])
    .properties(title="Uso de RAM (%)")
)

disk_chart = (
    alt.Chart(st.session_state.data)
    .mark_line(color="#1E88E5")
    .encode(x="Hora:N", y="Disco:Q", tooltip=["Hora", "Disco"])
    .properties(title="Uso de Disco (%)")
)

col1.altair_chart(cpu_chart, use_container_width=True)
col2.altair_chart(ram_chart, use_container_width=True)
col3.altair_chart(disk_chart, use_container_width=True)


time.sleep(2)
st.rerun()
