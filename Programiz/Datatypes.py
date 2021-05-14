
#Python Numbers
#Check variable types and class
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))        #Returns a true or false 


#Python List
a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])      #Reads from a[0] to a[3], a[3] not included

# a[3] = [20]
print("a[3] = ", a[3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:])

#Can change lists
a = [1, 2, 3]
a[2] = 4
print(a)

#Tuples 
#tuple is the same as a list, except you cannot change tuples
t = (5,'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable, cannot edit values in the list
# --> t[0] = 10 

#Python Strings
s = "This is a string"
print(s)
s = '''A multiline
Hey
This is fun
string'''
print(s)

#Strings can be treated as a list of characters
# The array is immutable
s = 'Hello world!'

# s[4] = 'o'
print("s[4] = ", s[4])

# s[6:11] = 'world'
print("s[6:11] = ", s[6:11])

# Generates error
# Strings are immutable in Python
# --> s[5] ='d'


#Python Set
a = {5,2,3,1,4}

# printing set variable
print("a = ", a)

# data type of variable a - Class is set
print(type(a))

#Sets have unique values, they remove duplicates
a = {1,2,2,3,3,3}
print(a)        #Prints {1, 2, 3}

#Sets are unordered, so slicing does not work
# a[1] produces an error


#Python Dictionary
#Keys are assigned values --> 
d = {1:'value','key':2}     #d is a dictionary
print(type(d))

d = {1:'value','key':2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error, no key named 2 (but there is a value named 2)
#print("d[2] = ", d[2])


#Conversion between data types
float(5) #5.0
int(10.6)   #10
int(-10.6)  #-10
float('2.5') #2.5
str(25) #'2.5'
# int('1p') error --> needs to have compatible values
