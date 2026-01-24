import streamlit as st
import psutil
import time

st.set_page_config(layout="wide")

st.title("Linux System Dashboard")

cpu = psutil.cpu_percent()
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

col1, col2, col3 = st.columns(3)
col1.metric("CPU", f"{cpu}%")
col2.metric("RAM", f"{ram}%")
col3.metric("Disco", f"{disk}%")

time.sleep(2)
st.rerun()
