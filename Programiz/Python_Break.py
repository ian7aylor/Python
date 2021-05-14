#Breaks

# Use of break statement inside the loop
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

#Continue statement
# Program to show the use of continue statement inside loops

for val in "string":
    if val == "i":
        continue        #Essentially means skip back to the top
    print(val)

print("The end")