# Simple IF statements
age = 19

if age >= 18:
    print('You are old enough to vote.\nHave you registered to vote?')


# if-else statements: one of the two actions will always be executed
age = 17

if age >= 18:
    print('You are old enough to vote.\nHave you registered to vote?')
else:
    print('You are not old enough to vote.\nPlease return as soon as you turn 18.')


# if-elif-else statements: for more possible situations, but only one action is exected
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price =40
print(f'Your admission cost is ${price}.')


# elif blocks can be as many as you need
age = 70

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price =20
print(f'Your admission cost is ${price}.')


# Omitting the else block
# Python does not require an else block
age = 70

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price =20
print(f'Your admission cost is ${price}.')
# use final 'elif' instead of 'else' if a specific final condition exists


# Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese.')
# 3 independent tests, all executed

print('\nFinished making your pizza!')
