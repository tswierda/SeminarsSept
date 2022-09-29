"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """the function input is 2 strings that are combined and added to a dictionary. The output gives
     a key value pair where the first key gives the first word, the second key the second word and the third key the two combined words"""
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
print(function_2b("aap","noot"))