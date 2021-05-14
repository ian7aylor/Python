# Fibonacci sequence up to n-th term

n = int(input("How many terms? "))

# first two terms
x, y = 0, 1
i = 0

# check if the number of terms is valid
#x is the final result
if n <= 0:
   print("Please enter a positive integer")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(x)
else:
   print("Fibonacci sequence:")
   while i < n:
       print(x)
       combxy = x + y
       # update values
       x = y
       y = combxy
       i += 1