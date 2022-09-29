"""
Write a documentation for the simple function below. Your partner will have to
implement the function, without knowing the code. Send your partner the
documentation and see if he can work with it.
No cheating! Don't show or tell hem the code directly
"""
def function_2b(string_1, string_2):
    """Change the case of strings, concat the originals, and return a dict.

    Example:

    ```
    >>> string_1 = "Jared"
    >>> string_2 = "Frazier"
    >>> dict_of_strings = function_2b(string_1=string_1, string_2=string_2)
    >>> print(dict_of_strings)
    {'L': 'jared', 'U': 'FRAZIER', 'C': 'JaredFrazier'}
    ```

    Arguments:
        string_1: A string for which a lower case copy
            will be defined.
        string_2: A string for which an upper case copy will 
            be defined.

    Returns:
        A dictionary with strings of different case as 
        its value.
            L -- Lower case string 1.
            U -- Upper case string 2.
            C -- Concatenated string 1 and string 2.
    """

    lower = string_1.lower()
    upper = string_2.upper()
    combined = string_1 + string_2

    dict = {"L": lower,
            "U": upper,
            "C": combined}

    return dict
