"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2) ->dict:
    """
    Use 2 inputs strings to create dictionary containing 1 lower case string
    1 upper case string and the combined strings
    input:
    string_1 : type = String
    string_2 : type = String
    output:
    dict = dictionary containing first string as lower case
                                 second string as upper case
                                 combined strings as single string
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
    