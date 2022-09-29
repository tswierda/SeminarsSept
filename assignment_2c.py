"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z) -> dict:
    """
    Returns four different results of mathematical
    operations on the give inputs

    Inputs:
    w = number
    x = number
    y = number
    z = number

    Output:
    results = dictionary of 4 different mathematical
              combinations of the inputs
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
