# Modifying - Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# replacing a new first element
motorcycles[0] = 'ducati'
print(motorcycles)

# list.append('element') adds an element to the end of the list
# .append() does not affect other elements in the list
motorcycles.append('honda')

print(motorcycles)

# .append() makes it easy to build lists dynamically
# start by defining an empty list to put users in control, then append each new value
colors = []

colors.append('Red')
colors.append('Green')
colors.append('Blue')

print(colors)

# inserting elements into a list - list.insert(index, 'element')
colors.insert(0, 'White')
print(colors)

# removing elements from a list, permanently - del list[index]
del colors[0]
print(colors)

# removing elements from a list, and still use them - pop() method
colors.append('White')
print(colors)

# .pop() removes the last element, White, but still can be used
popped_color = colors.pop()

print(colors)
print(popped_color)

# .pop() example
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# .pop(index) to remove an item from any position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# when you want to delete an item from a list and not use that item in any way, use the del statement; 
# if you want to use an item as you remove it, use the pop() method

# removing an item by value - list.remove('element')
cities = ['warsaw', 'krakow', 'prague', 'budapest']
print(cities)

cities.remove('krakow')
print(cities)

# variable can be used with .remove() method
cities = ['warsaw', 'krakow', 'prague', 'budapest']
print(cities)
too_touristy = 'krakow'

# .remove() method removes an element but still can be used
cities.remove(too_touristy)
print('\ncities:', cities)
print(f'\n{too_touristy.title()} is too touristy for me!')
