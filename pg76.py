# Checking whether a value is in a list - 'value' in 'list'
requested_topping = ['mushrooms', 'onions', 'pineapple']
is_mushrooms_requested = 'mushrooms' in requested_topping
is_cheese_requested = 'cheese' in requested_topping

print(is_mushrooms_requested)
print(is_cheese_requested)
# --> useful for for creating a list of essential values and check if testing values match them


# Checking whether a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user in banned_users:
    print(f'{user.title()} is NOT allowed to comment.')

if user not in banned_users:
    print(f'{user.title()} is allowed to comment.')


# Boolean Expressions - True / False
print(type(is_mushrooms_requested))
