"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """Gets and prints the spreadsheet's header columns

    Parameters
    ----------
    w : float
        variable used in addition (x+y) and subtraction (x-y)
    x : float
        variable used in multiplication x*y and division x/y
    y : float
        variable used in multiplication x*y and division x/y
    z : float
        variable used in addition (x+y) and subtraction (x-y)

    Returns
    -------
    dict
        Diconary with keys "multiply", "divide", "add", "subtract" 
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
