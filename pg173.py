# modeling real-world objects

# 9-6. Ice Cream Stand
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

class IceCreamStand(Restaurant):
    '''creating a child class from parent class Restaurant'''

    def __init__(self, name, cuisine_type):
        '''
        initialize attributes of the parent class
        add an additional attribute specific to IceCreamStand
        '''
        super().__init__(name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'butter pecan', 'strawberry']
    
    def display_flavors(self):
        '''displays ice cream flavors'''
        print(f'Available flavors are: {self.flavors}.')

stand_1 = IceCreamStand('IcyStand', 'dessert')
stand_1.describe_restaurant()
stand_1.open_restaurant()
stand_1.display_flavors()

# 9-7. Admin
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

class Admin(User):
    '''creating child class from parent class User'''
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print(f'List of administrator\'s privileges: {self.privileges}')

admin = Admin('jimmy', 'son')
admin.describe_user()
admin.show_privileges()

# 9-8. Privileges
class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print(f'List of administrator\'s privileges: {self.privileges}')

class Admin(User):
    '''creating child class from parent class User'''
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

admin = Admin('jimmy', 'son')
admin.describe_user()
admin.privileges.show_privileges()

# 9-9. Battery Upgrade
class Car:
    '''A simple attempt to represent a car'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self):
        print('This car\'s gas tank has been filled.')

class Battery:
    '''a simple attempt to model a battery for an electric car'''

    def __init__(self, battery_size = 75):      # set default battery size to 75
        '''initialzie the battery's attributes'''
        self.battery_size = battery_size
        
    def describe_battery(self):
        '''print a statement describing the battery size'''
        print(f'This car has a {self.battery_size}-kWh battery.')
    
    def upgrade_battery(self):
        '''sets the battery capacity to 100-kWh'''
        if self.battery_size != 100:
            self.battery_size = 100
            print(f'The battery capacity has been upgraded to {self.battery_size}-kWh.')
        else:
            print('This battery is at 100-kWh capacity.')
    
    def get_range(self):
        '''print a statement about the range this battery provides'''
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        else:
            range = 'undefined'
        
        print(f'This car can go about {range} miles on a full charge.')

class ElectricCar(Car):
    '''represent aspects of a car, specific to electric vehicles'''

    def __init__(self, make, model, year):
        '''
        initialize attributes of the parent class
        then initialize attributes specific to an electric car
        '''
        super().__init__(make, model, year)
        self.battery = Battery()    # adding an attribute that is a new instance of the class Battery

elec_1 = ElectricCar('KIA', 'E-Soul', '2022')
print(elec_1.get_descriptive_name())
elec_1.battery.describe_battery()
elec_1.battery.get_range()
elec_1.battery.upgrade_battery()
elec_1.battery.describe_battery()
elec_1.battery.get_range()
