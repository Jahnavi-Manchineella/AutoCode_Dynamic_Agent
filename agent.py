
from engine.generator import generate_code
from engine.validator import validate
from engine.benchmark import benchmark
from engine.optimizer import optimize

MAX_ATTEMPTS = 3

def run_agent(task: str):
    for attempt in range(1, MAX_ATTEMPTS + 1):
        code = generate_code(task, attempt)

        valid, error = validate(code, task)
        if not valid:
            continue

        metrics = benchmark(code, task)
        optimized = optimize(code, task)
        opt_metrics = benchmark(optimized, task)

        return {
            "success": True,
            "code": optimized,
            "metrics": {
                "baseline": metrics,
                "optimized": opt_metrics
            },
            "explanation": f"Code generated dynamically and optimized after passing validation in attempt {attempt}."
        }

    return {
        "success": False,
        "error": "Failed to generate correct code after multiple attempts."
    }
