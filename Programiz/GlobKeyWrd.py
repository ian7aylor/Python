
#Changing Global Variable From Inside a Function using global
c = 0 # global variable

def add():
    global c
    c = c + 2 # increment by 2
    print("Inside add():", c)

add()
print("In main:", c)

#For global variables across Python modules can create a config.py file and store global variables there

#Using a Global Variable in Nested Function
def foo():
    x = 20

    def bar():
        global x
        x = 25
    
    print("Before calling bar: ", x)
    print("Calling bar now")
    bar()
    print("After calling bar: ", x)

foo()
print("x in main: ", x)


#Test

global f
f = 2
def yes(f):
    f += 4
    
    return f
b = yes(f)
print(b)