# Copying a list
my_food  = ['pizza', 'KFC', 'paella', 'bibimbop', 'cheese cake', 'carbonara']
friend_food = my_food[:]

print(f'My favorite food are:\n{my_food}.')
print(f'My friend\'s favorite food are:\n{friend_food}.')

my_food.append('chicken wings')
friend_food.append('hot pot')

print(f'My favorite food are:\n{my_food}.')
print(f'My friend\'s favorite food are:\n{friend_food}.')

# 'friend_food = my_food' will associate new variables to both lists

# 4-10. Slices
food  = ['pizza', 'KFC', 'paella', 'bibimbop', 'cheese cake', 'carbonara', 'fried egg']


print('\nHere are the first three itmes in the list:')
for item in food[:3]:
    print(item)

mid = int((len(food)+1)/2)

print('\nHere are the middle three itmes in the list:')
for item in food[mid-2:mid+1]:
    print(item)

print('\nHere are the last three itmes in the list:')
for item in food[-3:]:
    print(item)

# 4-11. My Pizzas, Your Pizzas
my_pizzas = ['four cheese', 'carbonara', 'bbq']
friend_pizzas = my_pizzas[:]

my_pizzas.append('honey mustard')
friend_pizzas.append('chocolate')

print('\n')
print(f'My pizzas are:\n{my_pizzas}.')
print(f'My friend\'s pizzas are:\n{friend_pizzas}.')

# 4-12. More Loops
items = [] # random list

for item in items:
    print(item)
