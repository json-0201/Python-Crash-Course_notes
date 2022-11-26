# Tuples - list of immutable values (list of items that cannot change)
# Tuples - define using ()

dim = (200, 50)
print(dim[0])
print(dim[1])

# python returns error when trying to change value of tupple
# dim[0] = 250

# Tuple with one element - include a trailing comma
my_t = (3,)

# looping through all values in a tuple - same as list
for value in dim:
    print(value)

# writing over a tuple - redefine the entire tuple
dim = (200, 50)
print('oriignal dimension:')
for value in dim:
    print(value)

dim = (300,150)
print('modified dimension:')
for value in dim:
    print(value)

# 4-13. Buffet
buffet_food = ('rice', 'noodle', 'soup', 'tofu', 'meatball')
for food in buffet_food:
    print(food)

buffet_food = ('rice', 'noodle', 'soup', 'tofu', 'meatball', 'goulash', 'chicken')
for food in buffet_food:
    print(food)

buffet_food[1] = 'ice cream' # python returns an error
