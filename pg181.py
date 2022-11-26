# 9-13. Dice
from random import randint, choice

class Die:
    '''simple model of a die'''

    '''initialize an attribute sides'''
    def __init__(self, sides = 6):
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))

die_6 = Die()
die_10 = Die(10)
die_20 = Die(20)

for i in range(10):
    die_6.roll_die()
print('\n')

for i in range(10):
    die_10.roll_die()
print('\n')

for i in range(10):
    die_20.roll_die()
print('\n')


# 9-14. Lottery
rand_tuple = ('1', 'A', '4', 'F', '13', 'E', '11', 'G', '3', '9', 'I', '2', '23', '6', '15')

def choose_four(tuple):
    print('Any ticket matching the following four numbers or letters wins a price!:')
    for i in range(4):
        rand1, rand2, rand3, rand4 = choice(tuple), choice(tuple), choice(tuple), choice(tuple)
    print(f'\t{rand1}, {rand2}, {rand3}, {rand4}')

choose_four(rand_tuple)
print('\n')

# 9-15. Lottery Analysis
rand_tuple = ('1', 'A', '4', 'F', '13', 'E', '11', 'G', '3', '9', 'I', '2', '23', '6', '15')
my_ticket = ('1', 'A', '4', 'F', '13', 'E', '11', 'G', '3', '9', 'I', '2', '23', '6', '15')

def choose_four(tuple):
    print('Any ticket matching the following four numbers or letters wins a price!:')
    for i in range(4):
        rand1, rand2, rand3, rand4 = choice(tuple), choice(tuple), choice(tuple), choice(tuple)
    print(f'\t{rand1}, {rand2}, {rand3}, {rand4}')

    winning_list = (rand1, rand2, rand3, rand4)

    return winning_list

winning_list = choose_four(rand_tuple)

count = 0
while True:
    my_list = []

    my_list.append(choice(my_ticket))
    my_list.append(choice(my_ticket))
    my_list.append(choice(my_ticket))
    my_list.append(choice(my_ticket))

    my_tuple = tuple(my_list)
    print(my_tuple)

    if sorted(my_tuple) == sorted(winning_list):
        print('You have won the lottery!')
        print(f'number of iterations: {count}')
        
        break
    
    count += 1

# 9-16. Python Module of the Week
# https://pymotw.com/
