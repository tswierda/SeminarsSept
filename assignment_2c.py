"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    '''
    Args:
        w: Non-zero Integer
        x: Non-zero Integer
        y: Non-zero Integer
        z: Non-zero Integer

    Returns: Dict with four entries:
            'multiply': x multiplied by y,
            'divide': x divided by y,
            'add': w added to z
            'subtract: w subtracted by z

    '''

    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
