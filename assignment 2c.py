"""
This is the function to make four imput variables do four different math operations by the order of  
multiplication, division, addition, subtraction.
For multiplication, use the second * third variables.
For division, use the second / third variables.
For addition, use the first + fourth variables.
For subtraction, use the first - fourth variables.
Then, put the results in a dictionary.
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