"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
    This function performs the following operations:
    multiplication on x and y,
    division on x by y,
    addition of w and z,
    and subtraciton of w by z.
    Args:
        w: input for sum and subtraction (Minuend)
        x: input for multiplication and division (dividend)
        y: input for multiplication and division (divisor)
        z: input for sum and subtraction (subtrahend)

    Returns: Dictionary with the following key-value pairings:
            "multiply": multiplication,
            "divide": division,
            "add": addition,
            "subtract": subtraction}

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