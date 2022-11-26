# 3-1. Names
names = ['Paul', 'Kruti', 'Julie', 'Elvin']

for i in range(len(names)):

    print(names[i].title())

# 3-2. Greetings
for i in range(len(names)):

    message = f'Hey {names[i]}, what are you up to?'
    print(message)

# 3-3. Your Own List
transportation = ['bike', 'train', 'bus', 'airplane', 'walking']
for i in range(len(transportation)):

    message = f'My favorite type of transportation is {transportation[i].title()}!'
    print(message)
    