"""
Function that takes 4 integers(w, x, y, z) as input and
then does the following computations:
1)x times y
2)x divided by y
3)w times z
4)w minus z
The results are stored in a dictionary  with the following order:
                "multiply": multiplication,
               "divide": division,
               "add": addition,
               "subtract": subtraction
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
