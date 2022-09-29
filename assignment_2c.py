"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Arguments: 
    w, x, y, z; numerical values (int or float).

    Performs the following:
    - multiplication of x and y
    - division of x by y 
    - addition of z to w
    - subtracts z from w

    Returns: 
    dictionary with keys "multiply", "divide", "add", and "subtract", with as values
    the result of the corresponding performed mathematical operations 
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
