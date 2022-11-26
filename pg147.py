# passing an arbitrary number of arguments
# when you don't know how many arguments a function expects
#(*parameters)
def make_pizza(*toppings):
    '''print the list of toppings that have been requested'''
    print(toppings.title())

# *parameters ---> python makes an empty tuple and stores whatever values it receives
# convention ---> *args

def make_pizza(*toppings):
    '''print the list of toppings that have been requested'''
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print(f'\t{topping.title()}')

make_pizza('pepperoni')
make_pizza('mushrooms', 'cheese')
make_pizza('pineapples', 'green peppers', 'jamon')

# making positional and arbitrary arguments
# Python matches positional and keyword arguments first and then collects any remaining arguments in the final parameter
def make_pizza(size, *toppings):
    '''summarize the pizza to be made'''
    print(f'\nMaking {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'\t{topping.title()}')

make_pizza(9, 'pepperoni')
make_pizza(12, 'mushrooms', 'cheese')
make_pizza(24, 'pineapples', 'green peppers', 'jamon')

# using arbitrary keyword arguments
# functions that accept as many key-value pairs as the calling statement provides
# **parameter
def build_profile(first, last, **user_info):
    '''build a dictionary containing everything we know about the user'''
    user_info['first name'] = first.title()
    user_info['last name'] = last.title()
    return user_info

# **user_info creates empty dictionary called user_info
# convention ---> **kwargs

user_profile = build_profile('albert', 'einstein',
                            location = 'princeton',
                            field = 'physics')

print(user_profile)

# 8-12. Sandwiches
def show_ingredients(*ingredients):
    for ingredient in ingredients:
        print(f'\nAdding {ingredient.title()} to your sandwich!')

show_ingredients('ham')
show_ingredients('ham', 'cheese')
show_ingredients('ham', 'cheese', 'tomato')

# 8-13. User Profile
def user_profile(first, last, **user_info):
    user_info['first name'] = first.title()
    user_info['last name'] = last.title()
    return user_info

my_profile = user_profile('jimmy', 'son', height = '168cm', weight = '67kg', hobby = ['travel', 'dance', 'guitar'])
print('\nInformation about myself:')
for key, value in my_profile.items():
    print(f'\t{key}: {value}')

# 8-14. Cars
def car_info(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model name'] = model_name
    return car_info

car_1 = car_info('KIA', 'SOUL', color = 'white', crashed = 'yes')
print(car_1)
