# Classes
# object-oriented programming

# classes represent real-world things and situations
# objects are based on the classes

# instantiation - making an object from a class
# instances of a class

# Classes make life easier for you and the other programmers you’ll work with as you take on increasingly complex challenges

# creating and using a class
# capitalized names refer to classes in python
class Dog:
    '''a simple attempt to model a dog'''   # class description using docstring

    # A function that’s part of a class is a method
    # __init__() method - special method that Python runs automatically whenever creating a new instance based on the Dog class
    # __init__ method lets the class initialize the object’s attributes and serves no other purpose. It is only used within classes
    # self - reference to the instance itself; it gives the individual instance access to the attributes and methods in the class
    # self is passed automatically, no need to pass it
    # self.variable - available to every method in the class
    # Variables that are accessible through instances like this are called attributes
    def __init__(self, name, age):
        '''initialize name and age attributes'''
        self.name = name
        self.age = age
    
    def sit(self):
        '''simulate a dog sitting in response to a command'''
        print(f'{self.name} is now sitting.')
    
    def roll_over(self):
        '''simulate rolling over in response to a command.'''
        print(f'{self.name} rolled over!')

# class - a set of instructions for how to make an instance

# making an instance from a class
# instance = class(parameters), lowercase
dog_1 = Dog('Willie', 6)

# The __init__() method creates an instance representing a particular dog and sets the name and age attributes using the values provided

print(f'My dog\'s name is {dog_1.name}.')
print(f'My dog is {dog_1.age} years old.')
print('\n')


# accessing attributes
# use dot notation to access the attributes of an instance
print(dog_1.name.title(), '\n')

# calling methods
# dot notation to call any method defined in a class
dog_1.sit()
dog_1.roll_over()

# creating multiple instances
dog_1 = Dog('Willie', 6)
dog_2 = Dog('Lucy', 3)

print(f'My dog\'s name is {dog_1.name}.')
print(f'My dog is {dog_1.age} years old.')
dog_1.sit()

print(f'\nYour dog\'s name is {dog_2.name}.')
print(f'Your dog is {dog_2.age} years old.')
dog_2.sit()

# 9-1. Restaurant
class Restaurant:
    '''a simple attempt to model a restaurant'''

    def __init__(self, name, cuisine_type):
        '''initialize name and cuisine type attributes'''
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''prints the name and cuisine type of a restaurant'''
        print(f'\nThe restaurant is called {self.name.title()} and it serves {self.cuisine_type.title()} food.')
    
    def open_restaurant(self):
        '''prints that the restaurant is open'''
        print(f'{self.name.title()} is open now.')
    
rest_1 = Restaurant('Chef Wong', 'chinese')


rest_1.describe_restaurant()
rest_1.open_restaurant()


# 9-2. Three Restaurants
rest_1 = Restaurant('Chef Wong', 'chinese')
rest_2 = Restaurant('wing stop', 'american')
rest_3 = Restaurant('Taco Bell', 'mexican')

rest_1.describe_restaurant()
rest_2.describe_restaurant()
rest_3.describe_restaurant()

# 9-3. Users
class User:
    '''a simple attempt to model a user'''

    def __init__(self, first_name, last_name):
        '''initialize first name and last name attributes'''
        self.first_name = first_name
        self.last_name = last_name
    
    def describe_user(self):
        '''prints out user info'''
        print(f'\nfirst name: {self.first_name.title()}, last name: {self.last_name.title()}')
    
    def greet_user(self):
        '''simple greeting'''
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!')

user_1 = User('jimmy', 'son')
user_2 = User('krutu', 'nakrani')
user_3 = User('paul', 'amil')
user_4 = User('elvin', 'voung')

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
user_4.describe_user()
user_4.greet_user()
