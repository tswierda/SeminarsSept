"""
Arguments two string values you want to store and combine

Returns a dictionary that contains first string value in lower case (L), second string value in upper case (U) and the combined 
outcome of both string inputs (C). 
"""
def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
