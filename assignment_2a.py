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

"""
function_2b takes 2 strings as arguments
it transforms the first string to a lower case string and the second one to an 
upper case string it returns a dictionary with 3 elements, 
first one is the lowe case string, the second the upper case string
and the third one is a combination of them.
"""

var_2 = function_2b('Seminars', 'Borrel')['C']


'''
function_2c takes 4 inputs (w, x, y, z), it multiplies x and y, divides x by y, 
adds w and z, substracts z from w. It stores the results in a dictionary with 
keys multiply, divide, add, substract respectively.
'''
var_1 = function_2c(1000,10,100,-50)['add']


var_3 = str(function_2c(10,10,1000,10)["multiply"])+str(function_2b("CLS","ciao")["L"])


if var_1 == 950:
    print("Good job!")

if var_2 == "SeminarsBorrel":
    print("Well done!")

if var_3 == "10000cls":
     print("Excellent!")
