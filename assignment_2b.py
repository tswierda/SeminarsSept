"""
Function takes as inputs 2 words(strings)
the user can convert the first string to lowercase 
and the second string to uppercase.
also the function combines the two strings
a dictionary is created in the form:
                "L": lower,
               "U": upper,
               "C": combined
"""
def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
