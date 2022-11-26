# list - square brackets for collection of items in a particular order
# name of list - use plural (ex. letters, digits, names)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# access any element in a list by using its position/index, starting from [0]
# python returns a single item without square brackets
print(bicycles[0])
print(bicycles[0].title())

# index -1 = last item in the list
print(bicycles[-1])

# use f-strings to create a message using a value from a list
message = f'My first bike was a {bicycles[0].title()}.'
print(message)
