# writing to a file
# writing to an empty file
# To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file
# read mode ('r') [default], write mode ('w'), append mode ('a'), or a mode that allows you to read and write to the file ('r+')
filename = 'programming.txt'

with open(filename, 'w') as file_object:    # second argument 'w' - write
                                            # open() function automatically creates the file if it doesn't exist
    file_object.write('I love programming.')    # write() method to write a string to the file
'''
be careful opening a file in write mode ('w') because if the file does exist,
Python will erase the contents of the file before returning the file object
'''

# python can only write strings to a text file
# convert numerical data to string format str()

# writing multiple lines
# The write() function doesn’t add any newlines to the text you write
with open(filename, 'w') as file_object:       # add \n for newline
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')

# appending to a file
'''
If you want to add content to a file instead of writing over existing content,
you can open the file in append mode. When you open a file in append mode,
Python doesn’t erase the contents of the file before returning the file object.

Any lines you write to the file will be added at the end of the file.
If the file doesn’t exist yet, Python will create an empty file for you.
'''

with open(filename, 'a') as file_object:  # 'a' argument for append mode
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')

# programming.txt will contain added new two lines

# 10-3. Guest
filename_10_3 = 'guest.txt'

with open(filename_10_3, 'w') as file_object:
    name = input('Enter your name: ')
    file_object.write(name.title())

with open(filename_10_3, 'r') as file_object:
    contents = file_object.read()
print(f'name: {contents}\n')

# 10-4. Guest Book
filename_10_4 = 'guest_book.txt'
count = 1

with open(filename_10_4, 'w') as file_object:
    while True:
        name = input('Enter your name: \nenter \'q\' to exit.\n\tresponse: ')
        if name == 'q':
            break
        print(f'Welcome back, {name.title()}!')
        file_object.write(f'guest #{count}: {name.title()}\n')
        count += 1

with open(filename_10_4, 'r') as file_object:
    for line in file_object:
        print(line.strip())

# 10-5. Programming Poll
filename_10_5 = 'programming_poll.txt'
count = 1

with open(filename_10_5, 'w') as file_object:
    while True:
        reason = input('Why do you like programming?\nenter \'q\' to exit.\n\tresponse: ')
        if reason == 'q':
            break
        file_object.write(f'Response #{count}: {reason}.\n')
        count += 1

with open(filename_10_5, 'r') as file_object:
    for line in file_object:
        print(line.strip())
        