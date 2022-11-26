# working with classes and instances
# modifying attributes

# the Car class
class Car:
    '''a simple attempt to represent a car'''

    def __init__(self, make, model, year):
        '''initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        '''return a neatly formatted descriptive name'''
        descriptive_name = f'{self.year} {self.make} {self.model}'
        return descriptive_name
    
car_1 = Car('KIA', 'Soul', '2020')
print(car_1.get_descriptive_name())

# set a default value for an attribute
class Car:
    '''a simple attempt to represent a car'''

    def __init__(self, make, model, year):
        '''initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # no need to include in parameter

    def get_descriptive_name(self):
        '''return a neatly formatted descriptive name'''
        descriptive_name = f'{self.year} {self.make} {self.model}'
        return descriptive_name
    
    def read_odometer(self):
        '''prints a statement showing the car's mileage'''
        print(f'\nThis car\'s mileage is {self.odometer_reading}.')

car_1 = Car('KIA', 'Soul', '2020')
print('\n' + car_1.get_descriptive_name())
car_1.read_odometer()

# modifying attribute values

# modifying an attribute's value directly via instance
car_1.odometer_reading = 23     # instance.attribute = value
car_1.read_odometer()

# modifying an attribute's value throguh a method
# add a method that updates odometer reading
class Car:
    '''a simple attempt to represent a car'''

    def __init__(self, make, model, year):
        '''initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # no need to include in parameter

    def get_descriptive_name(self):
        '''return a neatly formatted descriptive name'''
        descriptive_name = f'{self.year} {self.make} {self.model}'
        return descriptive_name
    
    def read_odometer(self):
        '''prints a statement showing the car's mileage'''
        print(f'\nThis car\'s mileage is {self.odometer_reading}.')
    
    def update_odomter(self, mileage):
        '''
        set the odometer reading to the given value
        reject the change if it attempts to roll back odometer back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odomter!')

car_1 = Car('KIA', 'Soul', '2020')
car_1.update_odomter(2400)
car_1.read_odometer()

# incrementing an attribute's value through a method
class Car:
    '''a simple attempt to represent a car'''

    def __init__(self, make, model, year):
        '''initialize attributes to describe a car'''
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0   # no need to include in parameter

    def get_descriptive_name(self):
        '''return a neatly formatted descriptive name'''
        descriptive_name = f'{self.year} {self.make} {self.model}'
        return descriptive_name
    
    def read_odometer(self):
        '''prints a statement showing the car's mileage'''
        print(f'\nThis car\'s mileage is {self.odometer_reading}.')
    
    def update_odomter(self, mileage):
        '''
        set the odometer reading to the given value
        reject the change if it attempts to roll back odometer back
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\'t roll back an odomter!')

    def increment_odometer(self, miles):
        '''
        add the given amount to the odometer reading
        reject the change if it attempts to roll back odometer back 
        '''
        if miles > 0:
            self.odometer_reading += miles
            print(f'\t[Incrementing the mileage by {miles}...]')
        else:
            print('You can\'t roll back an odomter!')

        

car_1 = Car('KIA', 'Soul', '2020')
car_1.update_odomter(2400)
car_1.read_odometer()

car_1.increment_odometer(480)
car_1.read_odometer()

# 9-4. Number Served
class Restaurant:
    '''a simple attempt to model a restaurant'''

    def __init__(self, name, cuisine_type):
        '''initialize name and cuisine type attributes'''
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        '''prints the name and cuisine type of a restaurant'''
        print(f'\nThe restaurant is called {self.name.title()} and it serves {self.cuisine_type.title()} food.')
    
    def open_restaurant(self):
        '''prints that the restaurant is open'''
        print(f'{self.name.title()} is open now.')
    
    def set_number_served(self, number_served):
        self.number_served = number_served
    
    def increment_number_served(self, number_served):
        self.number_served += number_served
    
rest_1 = Restaurant('Chef Wong', 'chinese')
print('\n' + f'{rest_1.number_served}')     # default value of an attribute

rest_1.number_served = 2    # manually setting the value of an attribute
print(rest_1.number_served)

rest_1.set_number_served(29)    # calling a method to set the value of an attribute
print(rest_1.number_served)

rest_1.increment_number_served(31)
print(rest_1.number_served)

# 9-5. Login Attempts
class User:
    '''a simple attempt to model a user'''

    def __init__(self, first_name, last_name):
        '''initialize first name and last name attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        '''prints out user info'''
        print(f'\nfirst name: {self.first_name.title()}, last name: {self.last_name.title()}')
    
    def greet_user(self):
        '''simple greeting'''
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

user_1 = User('jimmy', 'son')

print('\n' + f'{user_1.login_attempts}')
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)
user_1.reset_login_attempts()
print(user_1.login_attempts)
