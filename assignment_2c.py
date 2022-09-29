"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    Function that does a bunch of mathematical operations with the input parameters and returns the results
    Parameters
    ----------
    w : float
        A random number
    x : float
        A random number
    y : float
        A random number
    z : float
        A random number
    
    Returns
    -------
    results : dict
        A dictionary with the results
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
