
def function_2c(w, x, y, z):
    """
    input: w, x, y, z
    muliplies x and y
    divides x/y
    adds w+z
    substracts w-z
    stores results in a dict
    output: dict
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
