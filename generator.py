
# This module is intentionally abstract.
# Replace `llm_generate` with OpenAI / Gemini / local LLM call.

def generate_code(task: str, attempt: int):
    prompt = f'''
You are a Python code generator.
Rules:
- Output only Python code
- One function named compute
- No file I/O, no network, no eval

Task:
{task}

Attempt: {attempt}
'''

    # Placeholder LLM output (developer plugs real model here)
    return '''
def compute(data):
    words = data.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq
'''
