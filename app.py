import streamlit as st
import papermill as pm
import os

st.set_page_config(page_title="Mpesa Notebook Runner", layout="centered")
st.title("📘 Run Reconciliation Notebook")

if st.button("▶️ Run Mpesa Notebook"):
    with st.spinner("Executing notebook..."):
        pm.execute_notebook(
            'MpesaV13062025.ipynb',
            'notebook_output.ipynb',
            parameters={}
        )
    st.success("✅ Notebook executed successfully.")

    if os.path.exists("mpesa_reconciliation_report.xlsx"):
        with open("mpesa_reconciliation_report.xlsx", "rb") as f:
            st.download_button("⬇️ Download Report", f, file_name="mpesa_reconciliation_report.xlsx")
    else:
        st.warning("Notebook ran but no report was generated.")