"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
    """
        Performs a multiplication, division, addition and substraction with input arguments.

        :param w: input argument for addition and substraction
        :param x: input argument for multiplication and division
        :param y: input argument for multiplication and division (must be > 0)
        :param z: input argument for addition and substraction
        :return: dictionary with results.
        results["multiply"] contains the product of x and y.
        results["divide"] contains the division of x by y.
        results["add"] contains the sum of w and z.
        results["substract"] contains the difference between w and z (w - z).
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
