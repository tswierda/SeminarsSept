"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """
    Arguments: string_1 - string of characters converted to lower case letters
    string_2 - string of characters converted to upper case letters
    Return - dictionary with three options:
    combined string of originals string "C"
    lower case of string_1  "L"
    uppercase of  string_2 "C"

    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
