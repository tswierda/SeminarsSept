"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    '''
    function_2b
    inputs: 
    - string_1 (str)
    - string_2 (str) 

    outputs:
    - dictionary with: 
        - C: string_1 and string_2 appended
        - L: string_1 in lower case
        - U: string_2 in upper case
    '''
    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
               "U": upper,
               "C": combined}

    return dict
