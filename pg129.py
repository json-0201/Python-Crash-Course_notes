# Functions
# blocks of code that are designed to do one specific job

# defining a function
# def func():
from email.policy import default


def greet_user():
    '''Display a simple greeting.''' # docstring - function description, ''' / """
    print('Hello there!')

greet_user() # function call - tells python to execute the code in the function

# passing information to a function
def greet_user(username):
    '''Display a simple greeting.'''
    print(f'Hello there, {username.title()}!')

greet_user('Jimmy Son')

# arguments and parameters
# parameter - a piece of information the function needs to do its job (ex. username)
# argument - value for defined parameter (ex. Jimmy Son)

# 8-1. Message
def display_message():
    '''simple display of a sentence about what I learned in this chapter'''
    print('I have learned nothing, so far.')

display_message()

# 8-2. Favorite Book
def favorite_book(book, author):
    '''simple display of my favorite book'''
    print(f'My favorite book is {book.title()} by {author.title()}.')

favorite_book('animal farm', 'george orwell')

# passing arguments
# positional arguments

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

# multiple function calls

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
# order matters in positional arguments

# keyword arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type = 'hamster', pet_name = 'harry') # specifying the parameters
# order does not matter in keyword arguments

# default values for parameters
# equivalent function calls
def describe_pet(pet_name, animal_type = 'dog'):    # default value for animal_type is dog
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name = 'willie') # positional arguments still valid
describe_pet('willie') # same result

describe_pet(pet_name='harry', animal_type='hamster') # add an argument to change default parameter value
describe_pet('harry', 'hamster') # same result

# avoiding argument errors
# describe_pet() - returns error [no arguments entered]

# 8-3. T-Shirt
def make_shirt(size, text):
    '''simple display of t-shirt size and text on it'''
    print(f'\nYour t-shirt size is {size} with {text.title()} written on it.')

make_shirt('X-Large', 'You only live once')

# 8-4. Large Shirts
def make_shirt(size = 'Large', text = 'I love Python'):
    '''simple display of t-shirt size and text on it'''
    print(f'\nYour t-shirt size is {size} with {text} written on it.')

make_shirt() # use default values
make_shirt('Large') # positional argument + default
make_shirt(size = 'Medium') # keyword argument + default
make_shirt('Small', 'Hip-Hop is a culture.')

# 8-5. Cities
def describe_city(name, country = 'USA'):
    '''simple display of a city and its country'''
    if country == 'USA':
        print(f'\n{name.title()} is in {country}.')
    else:
        print(f'\n{name.title()} is in {country.title()}.')

describe_city('Oslo', 'Norway')
describe_city(country = 'Spain', name = 'Madrid')
describe_city('Los Angeles')
