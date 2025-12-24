
import streamlit as st
from engine.agent import run_agent

st.set_page_config(page_title="AutoCode Dynamic Agent", layout="wide")
st.title("🧠 AutoCode: Dynamic Self-Correcting Code Agent")

task = st.text_area("Describe the Python task", "Count word frequency in a string")
run = st.button("Run AutoCode")

if run:
    with st.spinner("Running AutoCode agent..."):
        result = run_agent(task)

    if not result['success']:
        st.error(result['error'])
    else:
        st.subheader("Generated Code")
        st.code(result['code'], language="python")

        st.subheader("Performance")
        st.json(result['metrics'])

        st.subheader("Explanation")
        st.write(result['explanation'])
