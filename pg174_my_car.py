# importing classes is an effective way to program
# keep your main program file clean and easy to read

from pg174_car import Car

my_new_car = Car('kia', 'soul', 2020)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_new_car.update_odometer(49)
my_new_car.read_odometer()

my_new_car.increment_odometer(1)
my_new_car.read_odometer()
