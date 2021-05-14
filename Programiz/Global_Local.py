#Create a Global Variable
x = "global"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)

#Local Variables
#Can use global and local variables in the same function