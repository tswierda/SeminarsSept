"""
In this short exercise you will practice dealing with a merge conflict.
Finish the lower_case function and push your changes to the Github repository.
The fastest one to push is lucky, the others will most likely get a merge
conflict. See if you can fix it :)
"""

import string


def lower_case(string):

    """
    Argument:
    string -- text you want to turn into lower case

    Returns:
    lower_string -- lower case version of string

    """

    ### your code starts here
# *1: ord()
# *2：chr()
# ASCII：A-Z：65-90 ； a-z:97-122
    lower_string = []
    for i in string:
        if 65<= ord(i) <= 90:
            lower=ord(i)+32
            lower_string.append(chr(lower))
        else:
            lower_string.append(i)

    ### your code ends here

    return lower_string


"""
Do the same thing again with upper_case, but change the order so everyone
experiences at least 1 merge conflict.
"""

def upper_case(string):
    """
    Argument:
    string -- text you want to turn into upper case

    Returns:
    upper_string -- upper case version of string

    """

    ### your code starts here
    upper_string = []
    for i in string:
        if 97<= ord(i)<= 122:
            upper=ord(i)-32
            upper_string.append(chr(upper))
        else:
            upper_string.append(i)
    ### your code ends here

    return upper_string
