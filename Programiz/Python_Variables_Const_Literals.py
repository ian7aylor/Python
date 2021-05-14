import constant


#Python Variables, Constants, and Literals
number = 10
number = 1.1

#Declaring and assigning value to a variable

website = "apple.com"
print(website)

#Assign a new value to website
website = "programiz.com"

print(website)

#Can print multiple variables in a row
a, b, c = 5, 3.2, "Hello"

print (a)
print (b)
print (c)

#Can set variables equal to same value
x = y = z = "same"

print (x)
print (y)
print (z)

#access constants from another python script
#Captial letters should declare a constant
print(constant.PI)
print(constant.GRAVITY)



#Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2

#Complex Literal 
x = 3.14j +5

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)    #prints real and imaginary components of the literal

#String Literals
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)


#Boolean literals
x = (1 == True)         #Uses conditional operator, "is 1 = to True?"
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

#Special Literals
drink = "Available"
food = None        #None means field has not been created

#Definition for menu function
def menu(x):
    if x == drink:
        print(drink)
    elif x == food:
        print(food)

menu(drink)
menu(food)

#Literal Collections
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)   #Print list example
print(numbers)  #Print tuple example    
print(alphabets) #Print dictionary example
print(vowels)   #Print set example