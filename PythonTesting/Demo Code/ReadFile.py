# Reading a File Line by Line in Python and reverse it in o/p.
lines = []
rev = ""

file = open('File_Demo.txt', 'r')
lines = file.readlines()
print("{}{}".format("Content in File is ", lines))

for i in lines:
    rev = i + rev

print("{}{}".format("Reversed Content of the File is:", rev))

file.close()