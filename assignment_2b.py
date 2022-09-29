"""
input = string1, string2
changes string 1 into lowercase
changes string2 into uppercase
creates a dict with L: string1, U: string2, C: strings combined
return dict
"""
def function_2b(string_1, string_2):

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
