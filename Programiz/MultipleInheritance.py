
'''
A class can be derived from more than one base class in Python, similar to C++. This is called multiple inheritance.
In multiple inheritance, the features of all the base classes are inherited into the derived class. 
The syntax for multiple inheritance is similar to single inheritance.



'''
#Multiple Inheritance
#Multiderived has access to features of Base1+Base2+MultiDerived

class Base1:
    pass

class Base2:
    pass

class MultiDerived(Base1, Base2):
    pass

#Multilevel Inheritance
#Derived2 has access to Derived 1 attributes which has access to base
class Base:
    pass

class Derived1(Base):
    pass

class Derived2(Derived1):
    pass