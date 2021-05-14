
#Opening Files in Python
f = open("test.txt", encoding = 'utf-8')    # open file in current directory
#f = open("C:/Python38/README.txt")  # specifying full path
# f = open("test.txt")      # equivalent to 'r' or 'rt'
# f = open("test.txt",'w')  # write in text mode
# f = open("img.bmp",'r+b') # read and write in binary mode

# perform file operations
f.close()


#Safer way
try:
   f = open("test.txt", 'w', encoding = 'utf-8')
   # perform file operations
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
finally:
   f.close()