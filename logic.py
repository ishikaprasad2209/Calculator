def calculate(expression):
    try:
        result = eval(expression)  # Note: Be cautious with eval in production.
        return result
    except Exception:
        return "Error"
