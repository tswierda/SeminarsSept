"""
In this short exercise you will practice dealing with a merge conflict.
Finish the lower_case function and push your changes to the Github repository.
The fastest one to push is lucky, the others will most likely get a merge
conflict. See if you can fix it :)
"""

def lower_case(string):
    """
    Argument:
    string -- text you want to turn into lower case

    Returns:
    lower_string -- lower case version of string

    """
    lower_string = string.lower()

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

    upper_string = ""
    for c in string:
        if( c >= 'a' and c <= 'z' ):
            upper_string += chr(ord(c) - ord('a') + ord('A'))
        else:
            upper_string += c

    return upper_string

def main():
    print(lower_case("AbC"))
    print(upper_case("AbC"))


if __name__ == "__main__":
    main()

