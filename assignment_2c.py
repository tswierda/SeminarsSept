"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Arguments:
    w - first argument for addition and subtraction addition = w + z  subtraction = w - z
    x - first argument for multiplication and division x*y and x/y
    y - second argument for multiplication and division x*y and x/y cannot be 0
    z - second argument for addition and subtraction addition = w + z  subtraction = w - z
    Return - results of mathematical operations
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
