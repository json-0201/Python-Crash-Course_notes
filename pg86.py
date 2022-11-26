# Using if statements with lists
# Checking for special items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    print(f'Adding {topping}.')
print('\nFinished making your pizza!\n')


# Pizzeria runs out of green peppers
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    if topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:    
        print(f'Adding {topping}.')
print('\nFinished making your pizza!\n')


# Checking that a list is not empty - an empty list returns False when used in if statement
requested_toppings = []

if requested_toppings:
    for topping in requested_toppings:
        print(f'Adding {topping}.')
    print('\nFinished making your pizza!')
else:
    print('\nAre you sure you want a plain pizza?\n')


# Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'cucumber']

for topping in requested_toppings:
    if topping in available_toppings:
        print(f'Adding {topping}.')
    else:
        print(f'Sorry, we do not have {topping} available.')
print('\nFinished making your pizza!\n')
