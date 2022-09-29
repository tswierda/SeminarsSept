"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""

"""
    Argument:
    string_1 -- text you want to turn into lower case
    string_2 -- text you want to turn into upper case
    
    Returns:
    dictionary -- make string_1 lower case and string_2 upper case and return 
                  three pairs (U, string_2), (L, string_1), (C, string_1 + string2)
"""
def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
