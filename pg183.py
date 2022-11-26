# Files and Exceptions
# reading from a file
'''
When you want to work with the information in a text file, the first step is to read the file into memory.
You can read the entire contents of a file, or you can work through the file one line at a time.
'''

# reading an entire firle
# pi_digits.txt (pi to 30 decimal places, 10 decimal places per line)
# pi_digits.txt saved in the same directory as the code
with open('pi_digits.txt') as file_object:      # open() function - one argument needed: name of the file, returns an object representing the file
    contents = file_object.read()               # with - closes the file once access to it is no longer needed (when block finishes execution)
print(contents)                                 # read() method - read the contents of the file and store it as one long string in 'contents'

# in case of an last empty line, print with .rstrip()

# file paths
'''
To get Python to open files from a directory other than the one where your program file is stored,
you need to provide a file path, which tells Python to look in a specific location on your system.
'''
# pi_digits.txt is in the folder 'text_files', under current directory
# with open('text_files\\filename.txt') as file_object:...     # with open('folder\\filename')...

# absolute file path
# Absolute paths are usually longer than relative paths, so it’s helpful to assign them to a variable and then pass that variable to open():
# ex.
# file_path = 'C:\\Users\\Jimmy Son\\other_files\\text_files\\filename.txt'
# with open(file_path) as file_object:...

# backslashes in a file path often give errors - use double backslashes or use single backslash with 'r'
# file_path = r'C:\Users\Jimmy Son\other_files\text_files\filename.txt'
# file_path = 'C:\\Users\\Jimmy Son\\other_files\\text_files\\filename.txt'

# reading line by line
# assign the name of a file to a variable
filename = 'pi_digits.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)
        # an invisible newline character is at the end of each line in the text file
        # the print function adds its own newline each time it is called
        # print(line.rstrip())    # remove empty lines

# making a list of lines from a file
# using with, file object is only available by open() inside the with block
with open(filename) as file_object:
    lines = file_object.readlines()     # readlines() method takes each line from the file and stores it in a list

print('\n')
print(lines)    # lines is a list of every line from the file
for line in lines:      # prints each line from the file using for loop
    print(line.rstrip())

# working with a file's contents
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()  # strip() removes all whitespaces

print(pi_string)
print(len(pi_string))

# python reads everything from a text file as a string
# needs to convert numbers using int or float
pi_string = float(pi_string)
print(pi_string**2, '\n')

# large files: one million digits
# Python has no inherent limit to how much data you can work with; you can work with as much data as your system’s memory can handle

# if pi_string had 1 million decimals, we can print the first 50 by: print(f'{pi_string[:52]}...')
# print(len(pi_string)) will return 1000002 [includes 3 and .]

# is your birthday contained in pi?
filename2 = 'pi_1m.txt'
with open(filename2) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52])   # 50 decimals
print(len(pi_string))   # 1000002, 1 million decimals

birthday = input('Enter your b-day, in the form mmddyy: ')
if birthday in pi_string:
    print('Your b-day appears in the first million digits of pi!\n')
else:
    print('Your b-day doesn\'t appear in the first million digits of pi!\n')

# 10-1. Learning Python
filename3 = 'learning_python.txt'
with open(filename3) as file_object:
    contents = file_object.read()
print(contents, '\n')

with open(filename3) as file_object:
    for line in file_object:
        print(line.strip())
print('')   # add a single new line, print('\n') will add two lines

with open(filename3) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# 10-2. Learning C
# string.replace('word_old', 'word_new')
with open(filename3) as file_object:
    lines = file_object.readlines()
print('')

for line in lines:
    line = line.replace("Python", "C")      # python strings are immutable, need to re-define
    print(line.strip())
    