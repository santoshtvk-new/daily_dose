import streamlit as st
import pandas as pd
import cx_Oracle
import requests

st.set_page_config(layout="wide", page_title="Flow Data Validator")

# Sidebar: Data Source Selection
source_type = st.sidebar.selectbox("Data Source", ["CSV/Excel", "Oracle DB", "Databricks", "REST API"])
if source_type == "CSV/Excel":
    uploaded = st.sidebar.file_uploader("Upload file", type=["csv", "xlsx"])
    if uploaded:
        df = pd.read_csv(uploaded) if uploaded.name.endswith('.csv') else pd.read_excel(uploaded)
elif source_type == "Oracle DB":
    # Example connectors (credentials via st.secrets or input fields)
    conn_str = st.sidebar.text_input("Oracle Connection String")
    query = st.sidebar.text_area("SQL Query")
    if conn_str and query and st.sidebar.button("Fetch Data"):
        conn = cx_Oracle.connect(conn_str)
        df = pd.read_sql(query, conn)
        conn.close()
elif source_type == "REST API":
    endpoint = st.sidebar.text_input("API Endpoint")
    params = st.sidebar.text_area("Params (JSON)")
    if endpoint and st.sidebar.button("Fetch Data"):
        resp = requests.get(endpoint, params=eval(params))
        df = pd.DataFrame(resp.json())

# Display Data Table
if 'df' in locals():
    st.dataframe(df)
    st.write("Filter, Sort, and Compare tools here...")

    # Example: advanced filtering by user expressions
    expr = st.text_input("Filter Expression (e.g., col1>100 and col2=='A')")
    if expr:
        filtered = df.query(expr)
        st.dataframe(filtered)

# Flow Builder (Simplified)
# Allow user to define a flow as a list of steps
st.header("Flow Automation")
flow = []
step_type = st.selectbox("Step Type", ["Load Data", "Filter", "Sort", "Compare", "API Request"])
step_param = st.text_area("Parameters (JSON)")
if st.button("Add Step"):
    flow.append({"type": step_type, "params": step_param})
st.code(flow)

# Placeholder: execute flow (would need full DAG logic)
if st.button("Run Flow"):
    # Execute steps sequentially (in reality, implement function handlers)
    st.success("Flow executed (demo).")

st.caption("Prototype: Extend with visual canvas/graph, advanced diffing, integration plugins, flow save/load, scheduling, etc.")