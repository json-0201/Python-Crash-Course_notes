# 5-3.Alien Colors #1
from mailbox import Babyl


alien_color = 'red'
if alien_color == 'green':
    point = 5
if alien_color != 'green':
    point = 0
print(f'You have earned {point} points.')


# 5-4.Alien Colors #2
alien_color = 'yellow'
if alien_color == 'green':
    point = 5
else:
    point = 10
print(f'You have earned {point} points.')

# 5-4.Alien Colors #3
alien_color = 'red'
if alien_color == 'green':
    point = 5
elif alien_color == 'yellow':
    point = 10
else:
    point = 15
print(f'You have earned {point} points.')


# 5-6. Stages of Life
age = 28
if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'
print(f'Your current stage of life is {stage}.')


# 5-7. Favorite Fruit
fruits = ['kiwi', 'apple', 'mango', 'pear', 'peach']
if 'kiwi' and 'apple' in fruits:
    print('You really like kiwi and apple')
if 'mango' or 'banana' in fruits:
    print('You really like mango or banana, not sure which one!')
