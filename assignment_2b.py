"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
"""
function_2b takes two string inputs. The first string gets changed to all lower case
while the second string becomes all upper case. The function then adds the first and
second string together and returns all 3 strings back as a dictionary.
"""
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
