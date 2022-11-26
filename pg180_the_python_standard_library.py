# The Python standard library is a set of modules included with every Python installation

# ex. module 'random' - method 'randint(a,b)' [returns a randomly selected integer between a and b]
from random import randint
print(randint(5,10))

# ex. module 'random' - method 'choice(list/tuple)' [returns a randomly selected element in a list or tuple]
from random import choice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(choice(players), '\n')

# ex.
count = 0
active = True
print('The perfect combination is "7 Martina"')
while active:

    rand_int = randint(5,10)
    rand_player = choice(players)
    count += 1
    
    if rand_int == 7 and rand_player == 'martina':
        print(rand_int, rand_player.title(), f'\nFinally found the perfect combination in the {count}-th iteration!')
        active = False
        