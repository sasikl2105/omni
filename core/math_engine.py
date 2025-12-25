import re

def solve_math(expr: str):
    """
    Safely evaluate basic math expressions.
    Allowed: + - * / ( )
    """

    # remove unsafe characters
    expr = re.sub(r"[^0-9\.\+\-\*\/\(\) ]", "", expr)

    try:
        result = eval(expr, {"__builtins__": {}})
        return result
    except Exception:
        return "Invalid math expression."
