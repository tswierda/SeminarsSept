#from lib2to3.pytree import _Results
from assignment_2b import function_2b
from assignment_2c import function_2c

"""
Used the imported functions (function_2b and function_2c) and the documentation
provided by your teammates to generate the correct answers below. You can use
the following numbers and strings as input for the 2 functions:
[5, 10, 100, 1000, -50, 'seminars', 'Seminars', 'CLS', 'cLs', 'Borrel']
Run the script to see if you succeeded! PS: Multiple combinations are possible,
just give a correct one.
"""

var_1 = function_2c(1000, 1000, 50, 50)

var_2 = function_2b('Seminars', 'Borrel')

if var_1["subtract"] == 950:
    print("Good job!")

if var_2["C"] == "SeminarsBorrel":
    print("Well done!")

