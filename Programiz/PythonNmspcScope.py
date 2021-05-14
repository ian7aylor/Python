#Namespaces
#Name is the name we associate with the object
# Note: You may get different values for the id

a = 2
#both refer to the same object 2, so they have the same id().
print('id(2) =', id(2))
print('id(a) =', id(a))

# Note: You may get different values for the id
a = 2
print('id(a) =', id(a))

a = a+1
print('id(a) =', id(a))

print('id(3) =', id(3))

b = 2
print('id(b) =', id(b))
print('id(2) =', id(2))

#This is efficient as Python does not have to create a new duplicate object. 
#Functions are objects too, so a name can refer to them as well.
def printHello():
    print("Hello")
a = printHello
a()

#Namespaces

def outer_function():
    b = 20      #local namespace of this function
    def inner_func():
        c = 30  #local namespace to inner function

a = 10 #Global namespace