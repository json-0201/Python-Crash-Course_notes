# using aliases
# ... import ... as ...
from pg174_electric_car import ElectricCar as EC

my_tesla = EC('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

# finding your own workflow
'''
Python gives you many options for how to structure code in a large project.
It’s important to know all these possibilities so you can determine the best ways 
to organize your projects as well as understand other people’s projects.

When you’re starting out, keep your code structure simple.
Try doing everything in one file and moving your classes to separate modules once everything is working.
If you like how modules and files interact, try storing your classes in modules when you start a project.
Find an approach that lets you write code that works, and go from there.
'''
