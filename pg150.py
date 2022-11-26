# storing functions in modules
# storing your functions in a separate file allows you to hide the details of your program’s code and focus on its higher-level logic
# allows you to reuse functions in many different programs

# importing an entire module, same directory
# import module
# module_name.function_name()

# ex.
# import pizza ---> any function defined in pizza.py will now be available

# pizza.make_pizza(...)
# pizza.make_pizza(...)

##############################

# importing specific functions
# from module_name import function_name

# ex.
# from pizza import make_pizza, deliver_pizza, ...

# make_pizza(...) ---> dot notation no longer needed
# deliver_pizza(...) ---> dot notation no longer needed

##############################

# using as to give a module & function an alias
# import module_name as xyz
# from module_name import function as xyz

# ex.
# import pizza as pz
# from pizza import make_pizza as mp

# pz.make_pizza(...)
# mp(...)

##############################

# importing all functions in a module
# from module_name import *

# ex.
# from pizza import *
# make_pizza(...) ---> dot notataion not needed

# not the best approach
# Python may see several functions or variables with the same name, and instead of importing all the functions separately, it will overwrite the functions
