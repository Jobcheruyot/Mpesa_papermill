import streamlit as st
import papermill as pm
import os

NOTEBOOK_PATH = "MpesaV13062025.ipynb"

st.set_page_config(page_title="Mpesa Notebook Runner", layout="centered")
st.title("📘 Run Reconciliation Notebook")

if not os.path.exists(NOTEBOOK_PATH):
    st.error(f"Notebook not found: {NOTEBOOK_PATH}. Please upload it to your repo.")
else:
    if st.button(▶️ Run Mpesa Notebook"):
        with st.spinner("Executing notebook..."):
            pm.execute_notebook(
                NOTEBOOK_PATH,
                "notebook_output.ipynb",
                parameters={}
            )
        st.success("✅ Notebook executed successfully.")

        if os.path.exists("mpesa_reconciliation_report.xlsx"):
            with open("mpesa_reconciliation_report.xlsx", "rb") as f:
                st.download_button("⬇️ Download Report", f, file_name="mpesa_reconciliation_report.xlsx")
        else:
            st.warning("Notebook ran but no report was generated.")
