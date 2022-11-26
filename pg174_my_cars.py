# importing multiple classes from a module
from pg174_car import Car
from pg174_electric_car import ElectricCar

# importing an entire module
import pg174_car, pg174_electric_car
# for creating instance --> module_name.class_name()

# importing all classes from a module
# not recommended, avoid using this method if possible
# better to import an entire module and use - module_name.class_name()
from pg174_car import *
from pg174_electric_car import *

my_new_beetle = Car('volkswagen', 'beetle', 2019)
print(my_new_beetle.get_descriptive_name())

my_new_ioniq = ElectricCar('kia', 'ioniq 5', 2022)
print(my_new_ioniq.get_descriptive_name())

my_new_beetle = pg174_car.Car('volkswagen', 'beetle', 2019)
print(my_new_beetle.get_descriptive_name())

my_new_ioniq = pg174_electric_car.ElectricCar('kia', 'ioniq 5', 2022)
print(my_new_ioniq.get_descriptive_name())
