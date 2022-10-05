"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Takes two strings and returns a dictionary of 3 strings. string_1 in lowercase. String_2 in uppercase.
    A third string which is the concatenation of the operations on string_1 and string_2.


    Parameters
    ----------
    string_1: str
        a string to convert to all lowercase
    string_2: str
        a string to convert to all uppercase

    Returns
    ----------
    dict : dict
        a dictionary with keys: "L","U","C"
        contains string_1 in lowercase, string_2 in uppercase and the concatenation of string_1 and string_2 respectively

    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
    