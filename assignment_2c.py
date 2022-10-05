"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2c(w, x, y, z):
        """
    Takes 4 integers w,x,y and z. Returns a dictionary containing multiplication, division, addition
     and subtraction on these integers.


    Parameters
    ----------
    w : int
        integer
    x : int
        integer
    y : int 
        integer
    z : integer

    Returns
    ----------
    results : dict
        a dictionary with keys: "multiply","divide","add", "subtraction"
        contains multiplication of x,y; division of x,y; addition of w,z; subtraction of w,z respectively.

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
