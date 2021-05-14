import math
from math import pi     #can do this if all you want is the pi attribute
import sys

#printing Output 
print('This sentence is output to the screen')

a = 5
print('The value of a is', a)

"""This is how print works
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
Here, objects is the value(s) to be printed.
The sep separator is used between the values. It defaults into a space character.
After all values are printed, end is printed. It defaults into a new line.
The file is the object where the values are printed and its default value is sys.stdout (screen). Here is an example to illustrate this.
"""
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')


#Output formatting 

#Using str.format()
x = 5; y = 10
print('The value of x is {} and y is {}'.format(x,y))
#Curly braces are used as placeholders
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))

#Can use keyword arguments to format the string
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
x = 12.3456789
print('The value of x is %3.4f' %x) #prints at least 3 wide with 4 values to right of dec
print('The value of x is %3f' %x)   #prints at least 3 wide, no specification of values to right of dec

#Python Input
num = input('Enter a number: ')

sys.path        #Returns list of directory locations
