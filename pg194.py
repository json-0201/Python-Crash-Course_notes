# Exceptions
'''
Python uses special objects called exceptions to manage errors that arise during a program’s execution.
Whenever an error occurs that makes Python unsure what to do next, it creates an exception object.
If you write code that handles the exception, the program will continue running.
If you don’t handle the exception, the program will halt and show a traceback,
which includes a report of the exception that was raised.
'''

# handling the zero-division exception
# print(5/0)  # returns error with traceback
              # ZeroDivisionError is an exception object

# try-except blocks
try:            # if code in try block works, python skips over the except block
    print(5/0)
except ZeroDivisionError:       # if code in try block doesn't work, python looks for corresponding error in except block
    print('You can\'t divide by zero!')

# If more code followed the try-except block, the program would continue running

# using exceptions to prevent crashes
print('Give me two numbers, and I\'ll divide them.')
print('Enter \'q\' to quit.')

# try-except-else block
while True:
    first_number = input('\nfirst number: ')
    if first_number == 'q':
        break
    
    second_number = input('second number: ')
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print('You can\'t divide by zero!')
    
    else:
        print(f'{first_number} divided by {second_number} = {answer}')

'''
The try-except-else block works like this: Python attempts to run the code in the try block.
The only code that should go in a try block is code that might cause an exception to be raised.
Sometimes you’ll have additional code that should run only if the try block was successful;
this code goes in the else block.
The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try block.
By anticipating likely sources of errors, you can write robust programs that continue to run even when they encounter invalid data and missing resources.
Your code will be resistant to innocent user mistakes and malicious attacks.
'''

# handling FileNotFound exception
filename = 'alice.txt'

#with open(filename, encoding = 'utf-8') as f:  # file_obect as 'f'
#    contents = f.read()                        # encoding argument needed when system default encoding doesn't match the file encoding

# returns FileNotFound exception object

try:
    with open(filename, encoding = 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'The file {filename} does not exist.')
print('')

# analyzing text
# count the number of words in a text
# split() method for string - store words separated by space in a list
with open(filename, 'w') as f:      # create alice.txt and write 'Alice in Wonderland' (3 words)
    f.write('Alice in Wonderland')

try:
    with open(filename, encoding = 'utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'The file {filename} does not exist.')
else:
    words = contents.split()
    num_words = len(words)
    print(f'The file {filename} contains {num_words} words.')
print('')

# working with multiple files
# create a function for counting words in a file
def count_words(filename):
    '''count approximate number of words in a file'''
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f'The file {filename} does not exist.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} contains {num_words} words.')

filename = 'alice.txt'
count_words(filename)   # testing the function count_words()
print('')

filenames = ['alice_in_wonderland.txt', 'moby_dig.txt', 'little_women.txt', 'siddhartha.txt', 'moby_dick.txt']   # intentional error in name: moby_dig.txt
for file in filenames:
    count_words(file)
# the missing 'moby_dig.txt' does not affect on the rest of the program's execution
# try-except block: 1) users don't see error traceback 2) code execution doesn't stop

# failing silently
# 'pass' in except block will do nothing in the block
def count_words(filename):
    '''count approximate number of words in a file'''
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        #print(f'The file {filename} does not exist.')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} contains {num_words} words.')

print('')   
for file in filenames:
    count_words(file)   # function modified to do nothing for FileNotFoundError exception

# missing_files.txt
# modify function to save missing files in a separate file
def count_words(filename, missing_file):
    '''count approximate number of words in a file'''
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        with open(missing_file, 'a') as f:
            f.write(f'{filename}\n')
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} contains {num_words} words.')

with open('missing_files.txt', 'w') as f:
    f.write('The following are the missing files: \n')

print('')
filenames = ['alice_in_wonderland.txt', 'moby_dig.txt', '1984.txt', 'animal_farm.txt', 'little_women.txt', 'siddhartha.txt', 'moby_dick.txt']   # files don't exist
for file in filenames:
    count_words(file, 'missing_files.txt')

# deciding which errors to report
'''
Python’s error-handling structures give you fine-grained control over how much to share with users when things go wrong;
it’s up to you to decide how much information to share.
Well-written, properly tested code is not very prone to internal errors, such as syntax or logical errors.
But every time your program depends on something external,
such as user input, the existence of a file, or the availability of a network connection, there is a possibility of an exception being raised.
'''
