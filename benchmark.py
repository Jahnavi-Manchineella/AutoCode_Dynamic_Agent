
import time

def benchmark(code: str, task: str):
    local_env = {}
    exec(code, local_env)
    fn = local_env['compute']

    if 'text' in task.lower() or 'word' in task.lower():
        data = "hello world hello streamlit world " * 50000
    else:
        data = list(range(10**6))

    start = time.time()
    fn(data)
    end = time.time()

    return {"time_sec": round(end - start, 5)}
