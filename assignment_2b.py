"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1: str, string_2: str):
    """
    Parameters:
    string_1: a string
    string_2: a string

    Returns a dictionary with the following structure:
    'L': string_1, all lowercase
    'U': string_2, all uppercase
    'C': string_1 concatenated with string_2
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
