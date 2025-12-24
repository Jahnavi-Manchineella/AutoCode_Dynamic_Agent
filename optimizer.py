
# Optimizer prompts LLM again in real systems.
# Here we apply safe Pythonic optimizations.

def optimize(code: str, task: str):
    if 'word' in task.lower():
        return '''
from collections import Counter
def compute(data):
    return Counter(data.split())
'''
    return code
