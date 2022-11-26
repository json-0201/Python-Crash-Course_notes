# Organizing a list

# sort() method for sorting a list permanently
# sort() method sorts alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# sort() method in reverse direction
cars.sort(reverse=True)
print(cars)

# sorted() for sorting a list temporarily while maintaining the original list
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)
print(sorted(cars))
print(sorted(cars, reverse=True))
print(cars)

# reverse() method for printing a list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# len() function to find the length f a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
