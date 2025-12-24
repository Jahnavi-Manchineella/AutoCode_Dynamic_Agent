
# AutoCode Dynamic Agent

This is a research-grade dynamic code agent.

## Features
- Dynamic code generation (LLM-driven placeholder)
- Self-verification loop
- Repair attempts
- Sandboxed execution
- Performance benchmarking

## To Enable Real LLM
Replace `generate_code()` with calls to OpenAI / Gemini / local LLM.

## Run
```bash
pip install streamlit
streamlit run app.py
```
