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
input_2b=[-50, 10, 100, 1000]
input_2c=['seminars', 'Borrel']
var_1 = function_2c(input_2c)['add']

var_2 = function_2b(input_2b)["C"]

if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

