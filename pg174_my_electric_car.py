from pg174_electric_car import ElectricCar

my_new_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_new_tesla.get_descriptive_name())
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range()
