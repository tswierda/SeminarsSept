"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """Gets 4 numbers and returns a dictionary containing 4 key-value pairs.

    Args:
        w (number): a number
        x (number): a number
        y (number): a number
        z (number): a number

    Returns:
        dictionary: A dictionary with 4 entries: 'multiply', 'divide', 'add'
        and 'subtract'. Each entry has a value: x * y, x / y, w + z and w - z
        respectively.
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
