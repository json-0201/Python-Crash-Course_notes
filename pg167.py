# Inheritance

'''
If the class you’re writing is a specialized version of another class you wrote, you can use inheritance.
When one class inherits from another, it takes on the attributes and methods of the first class. 
The original class is called the parent class, and the new class is the child class. 
The child class can inherit any or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own.
'''

# the __init__() method for a child class
# the parent class must be part of the current file and must appear before the child class in the file
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

class ElectricCar(Car):     # class child class(parent class):
    '''represent aspects of a car, specific to electric vehicles'''

    def __init__(self, make, model, year):      # information required to make an instance from parent class
        '''initialize attributes of the parent class'''
        super().__init__(make, model ,year)     # super(). function allows you to call a method from the parent class, giving all attributes from parent class
                                                # super - superclass

tesla_1 = ElectricCar('tesla', 'model s', 2019)
print(tesla_1.get_descriptive_name())   # using a method from parent class

# defining attributes and methods for the child class
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

class ElectricCar(Car):     # class child class(parent class):
    '''
    represent aspects of a car, specific to electric vehicles
    then initialize attributes/methods specific to an electric car (child class)
    '''

    def __init__(self, make, model, year):      # information required to make an instance from parent class
        '''initialize attributes of the parent class'''
        super().__init__(make, model ,year)     # super(). function allows you to call a method from the parent class, giving all attributes from parent class
                                                # super - superclass
        self.battery_size = 75
    
    def describe_battery(self):     # only associated to class ElectricCar
        '''prints a statement describing the battery size'''
        print(f'This car has a {self.battery_size}-kWh battery.')    


tesla_1 = ElectricCar('tesla', 'model s', 2019)
tesla_1.describe_battery()

# overriding methods from the parent class
# You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class
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

class ElectricCar(Car):     # class child class(parent class):
    '''
    represent aspects of a car, specific to electric vehicles
    then initialize attributes/methods specific to an electric car (child class)
    '''

    def __init__(self, make, model, year):      # information required to make an instance from parent class
        '''initialize attributes of the parent class'''
        super().__init__(make, model ,year)     # super(). function allows you to call a method from the parent class, giving all attributes from parent class
                                                # super - superclass
        self.battery_size = 75
    
    def describe_battery(self):     # only associated to class ElectricCar
        '''prints a statement describing the battery size'''
        print(f'This car has a {self.battery_size}-kWh battery.')
    
    def fill_gas_tank(self):
        '''electric cars don't have gas tanks'''
        print('This car doesn\'t need a gas tank!')

car_1 = Car('Honda', 'Civic', 2017)
car_1.fill_gas_tank()   # method from parent class

tesla_1 = ElectricCar('tesla', 'model s', 2019)
tesla_1.fill_gas_tank()     # method from child class, overridden
# child classes retain what you need and override anything you don’t need from the parent class

# instances as attributes
# You can break your large class into smaller classes that work together
class Battery:
    '''a simple attempt to model a battery for an electric car'''

    def __init__(self, battery_size = 75):      # set default battery size to 75
        '''initialzie the battery's attributes'''
        self.battry_size = battery_size
    
    def describe_battery(self):
        '''print a statement describing the battery size'''
        print(f'This car has a {self.battry_size}-kWh battery.')

class ElectricCar(Car):
    '''represent aspects of a car, specific to electric vehicles'''

    def __init__(self, make, model, year):
        '''
        initialize attributes of the parent class
        then initialize attributes specific to an electric car
        '''
        super().__init__(make, model, year)
        self.battery = Battery(60)    # adding an attribute that is a new instance of the class Battery
                                    # setting a battery size to 60 kWh

tesla_1 = ElectricCar('tesla', 'model s', 2019)
print(tesla_1.get_descriptive_name())
tesla_1.battery.describe_battery()

########################################################################
class Battery:
    '''a simple attempt to model a battery for an electric car'''

    def __init__(self, battery_size = 75):      # set default battery size to 75
        '''initialzie the battery's attributes'''
        self.battery_size = battery_size
    
    def describe_battery(self):
        '''print a statement describing the battery size'''
        print(f'This car has a {self.battery_size}-kWh battery.')
    
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

tesla_1 = ElectricCar('tesla', 'model s', 2019)
print(tesla_1.get_descriptive_name())
tesla_1.battery.describe_battery()
tesla_1.battery.get_range()
