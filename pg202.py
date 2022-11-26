# Storing Data
'''
Many of your programs will ask users to input certain kinds of information.
You might allow users to store preferences in a game or provide data for a visualization.
Whatever the focus of your program is, you’ll store the information users provide in data structures such as lists and dictionaries.
When users close a program, you’ll almost always want to save the information they entered.
'''
# json module (JavaScript Object Notation)
# json module allows you to dump simple Python data structures into a file and load the data from that file the next time the program runs

# json.dump(data, file object) - write
import json # import json module
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json' # include extension .json in the file
with open(filename, 'w') as f:
    json.dump(numbers, f)

# json.load(file object) - read
filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

# saving and reading user-generated data
import json

username = input('Enter your name: ')
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
print(f'We\'ll remember you when you come back, {username}!')

filename = 'username.json'
with open(filename) as f:
    username = json.load(f)
print(f'Welcome back, {username}!')

# remember_me.py
import json
# Load the username, if it has been stored previously
# Otherwise, prompt for the username and store it
filename = 'username_2.json'
try:    # look for a file 'username.json'
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:   # if file doesn't exist, prompt the user for the input
    username = input('Enter your name: ')
    with open(filename, 'w') as f:
        json.dump(username, f)   
        print(f"We'll remember you when you come back, {username}!")
else:   # if file exists, prints out a greeting
    print(f'Welcome back, {username}!')

# Refactoring
# Refactoring makes your code cleaner, easier to understand, and easier to extend

# refactoring remember_me.py by dividing it into 3 functions
import json

def get_stored_username():
    '''get stored username if available'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''prompt for a new username'''
    username = input('Enter your name: ')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(filename, f)
    return username

def greet_user():
    '''greet the user by name'''
    username = get_stored_username()
    if username:
        print(f'Welcome back, {username}!')
    else:
        username = get_new_username()
        print(f'We\'ll remember you when you come back, {username}!')

greet_user()

# 10-11. Favorite Number
import json

print('')
fav_num = input('Enter your favorite number: ')
file_10_11 = 'favorite_number.json'
with open(file_10_11, 'w') as f:
    json.dump(fav_num, f)

with open(file_10_11) as f:
    user_fav_num = json.load(f)
print(f'I know your favorite number! It\'s {user_fav_num}!')

# 10-12. Favorite Number Remembered
import json

print('')
file_10_12 = 'favorite_number2.json'
try:
    with open(file_10_12) as f:
        user_fav_num = json.load(f)
except FileNotFoundError:
    with open(file_10_12, 'w') as f:
        fav_num = input('Enter your favorite number: ')
        json.dump(fav_num, f)
else:
    print(f'I know your favorite number! It\'s {user_fav_num}!')

# 10-13. Verify User
import json

def get_stored_username():
    '''get stored username if available'''
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    '''prompt for a new username'''
    username = input('Enter your name: ')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(filename, f)
    return username

def greet_user():
    '''greet the user by name'''
    username = get_stored_username()
    if username:
        verify_user = input(f'Are you \'{username}\'? (yes/no): ')
        if verify_user == 'yes':
            print(f'Welcome back, {username}!')
        else:
            username = get_new_username()
            print(f'Welcome back, {username}!')
            
    else:
        username = get_new_username()
        print(f'We\'ll remember you when you come back, {username}!')

greet_user()
