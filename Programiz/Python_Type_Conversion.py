#Implicit Type Conversion
num_int = 123       #int
num_flo = 1.23      #float

num_new = num_int + num_flo     #float

print("datatype of num_int:",type(num_int))
print("datatype of num_flo:",type(num_flo))

print("Value of num_new:",num_new)
print("datatype of num_new:",type(num_new))

#Addition of string(higher) data type and intger(lower) data type
num_int = 123
num_str = "456"

print("Data type of num_int:",type(num_int))
print("Data type of num_str:",type(num_str))

# This is an error, cannot implicity convert to correct type print(num_int+num_str)

#Explicit Type Conversion
num_int = 123       #integer
num_str = "456"     #string

print("Data type of num_int:",type(num_int))
print("Data type of num_str before Type Casting:",type(num_str))

num_str = int(num_str)      #type cast string to int
print("Data type of num_str after Type Casting:",type(num_str))

num_sum = num_int + num_str     #will produce an int

print("Sum of num_int and num_str:",num_sum)
print("Data type of the sum:",type(num_sum))