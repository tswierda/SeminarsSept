"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Function that makes string 1 all lowercase, string 2 all uppercase and returns both together with a combination of the two
    Parameters
    ----------
    string_1 : str
        A random string
    string_2 : str
        A random string
    
    Returns
    -------
    dict : dict
        A dictionary with string 1 as all lowercase, string 2 as all uppercase and a concatination of the two
    """
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
