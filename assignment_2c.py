"""
Arguments: w, x, y, z 

Returns a dictionary containing the following transformation labels and their outcomes
Multiply and divide x and y in respective order, add and substract for values x and y.
"""
def function_2c(w, x, y, z):

    multiplication = x * y
    division = x / y
    addition = w + z
    subtraction = w - z

    results = {"multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction}

    return results
