#Intro to statements

#can continue a statement with a \

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
    
a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

#Can do continuation with brackets as well
colors = ['red',
          'blue',
          'green']

#Can do multiple statements with semicolons
a = 1; b = 2; c = 3

#Mult-line comment without extra code
"""This is also a
perfect example of
multi-line comments"""

#Docstrings
def double(num):
    """Function to double the value"""
    return 2*num



x = double(3)
print(x)
#Access the doc string of a function with __doc__
print(double.__doc__)