
def validate(code: str, task: str):
    try:
        local_env = {}
        exec(code, local_env)
        assert 'compute' in local_env
        return True, None
    except Exception as e:
        return False, str(e)
