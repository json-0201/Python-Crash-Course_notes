# using a while loop with lists and dictionaries
# moving items from one list to another

unconfirmed_users = ['alice', 'brian', 'candace'] # users to be verified
confirmed_users = [] # to hold verified users

# verify users until there are no more unconfirmed users
# move each verified user into the list of confirmed users

while unconfirmed_users: # list is True as long as it is not empty
    current_user = unconfirmed_users.pop() # deletes and temporarily saves user (.pop() starts with the last item)

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user) # adds to the list of confirmed users

print('\nThe following user has been verified:')
for user in confirmed_users:
    print(user.title())

# removing all instances of specific values from a list
# list.remove(instance)
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print('\n', pets)

while 'cat' in pets:    # True while 'cat' exists in the list pets
    pets.remove('cat')
print(pets)

# filling a dictionary with user input
responses = {}

# flag to set the polling active
polling_active = True

while polling_active:
    # prompt for name and response
    name = input('\nEnter your name:')
    response = input('Enter your favorite mountain:')

    responses[name] = response # responses[name] = key, response = value (dictionary)

    repeat = input('Would you like to let another person respond? [yes/no]')
    if repeat == 'no':
        polling_active = False

print('\n---polling results---')
for name, response in responses.items():
    print(f'{name.title()}\'s favorite mountain is {response.title()}\n')

# 7-8. Deli
sandwich_orders = ['hawaiian', 'barbeque', 'egg', 'salmon', 'grilled cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Preparing your {current_sandwich} sandwich...')

    finished_sandwiches.append(current_sandwich)

print('\nFollowing sandwiches have been prepared:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich.title()} sandwich')

# 7-9. No Pastrami
sandwich_orders = ['hawaiian', 'pastrami', 'barbeque', 'pastrami', 'egg', 'salmon', 'grilled cheese', 'pastrami']
finished_sandwiches = []

print('\nSorry, Deli has run out of pastrami...')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Preparing your {current_sandwich} sandwich...')

    finished_sandwiches.append(current_sandwich)

print('\nFollowing sandwiches have been prepared:')
for sandwich in finished_sandwiches:
    print(f'\t{sandwich.title()} sandwich')

# 7-10. Dream Vacation
responses = {}

polling_active = True
while polling_active:
    name = input('\nEnter your name:')
    destination = input ('If you could visit one place in the world, wherewould you go?')

    responses[name] = destination
    
    repeat = input('\nWould you like the next person to take a poll? [yes/no]')
    if repeat == 'no':
        polling_active = False

print('\n---polling results---')
for name, destination in responses.items():
    print(f'{name.title()} would like to visit {destination.title()}.')
