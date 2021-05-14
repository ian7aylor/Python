#Lambda functions
# Program to show the use of lambda functions
double = lambda x: x * 2
'''
Same as 
def double(x):
   return x * 2
'''
print(double(5))

#lambda function used along with filter() and map()

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))   #Filters out even numbers from a list
print(new_list)

# Program to double each item in a list using map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)
