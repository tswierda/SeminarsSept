"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    This function does various mathematical operations: multiplication, division,
    addition and subtraction

    Input:
    w: float, will be multiplied by y and added/substracted to z
    x: float, will be divided by y
    y: float
    z: float, will be added/substracted by z

    Returns a dictionary with the results for each of the 4 operations, with keys
     'multiply', 'divide', 'add','subtract'

    """
    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
