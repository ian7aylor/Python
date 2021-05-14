#For Loop

'''
for val in sequence:
    Body of for
'''
# Program to find the sum of all numbers stored in a list
# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
#iterates through list of numbers and sums them together
for val in numbers:
    sum = sum+val

print("The sum is", sum)

#Range function (start, stop, step size)
print(range(10))
print(list(range(10)))              #10 values, 0-9
print(list(range(2, 8)))            # Goes 2-7, 7 is 8th position
print(list(range(2, 20, 3)))        # step size is 3


# Program to iterate through a list using indexing
genre = ['pop', 'rock', 'jazz']
print(range(len(genre)))
# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])
    
    
#For loop with else
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

#Can use a break statement rather than an else    
# program to display student's marks from record
student_name = 'Jules'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])   #Prints value associated with key
        break
else:
    print('No entry with that name found.')