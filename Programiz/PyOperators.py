
#Arithmetic Operators
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3 - Modulus
print('x // y =',x//y)

# Output: x ** y = 50625 - exponent
print('x ** y =',x**y)



#Comparison Operators
x = 10
y = 12

# Output: x > y is False
print('x > y is',x>y) 

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)


#Logical Operators
x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

#Bitwise Operators
""" 
Operator	Meaning	                Example
&	        Bitwise AND	            x & y = 0 (0000 0000)
|	        Bitwise OR     	        x | y = 14 (0000 1110)
~	        Bitwise NOT	            ~x = -11 (1111 0101)
^	        Bitwise XOR	            x ^ y = 14 (0000 1110)
>>	        Bitwise right shift	    x >> 2 = 2 (0000 0010)
<<	        Bitwise left shift	    x << 2 = 40 (0010 1000)

"""
#Assignment Operators
"""Operator	Example	Equivalent to
=	        x = 5	    x = 5
+=	        x += 5	    x = x + 5
-=	        x -= 5	    x = x - 5
*=	        x *= 5	    x = x * 5
/=	        x /= 5	    x = x / 5
%=	        x %= 5	    x = x % 5
//=	        x //= 5	    x = x // 5
**=	        x **= 5	    x = x ** 5
&=	        x &= 5	    x = x & 5
|=	        x |= 5	    x = x | 5
^=	        x ^= 5	    x = x ^ 5
>>=	        x >>= 5	    x = x >> 5
<<=	        x <<= 5	    x = x << 5
"""

#Special Operators

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)


#Membership Operators
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True - case sensitive
print('hello' not in x)

#Looks for keys
# Output: True
print(1 in y)

# Output: False
print('a' in y)