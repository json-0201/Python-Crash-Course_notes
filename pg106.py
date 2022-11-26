# Nesting
# A list of dictionaries
# dictionar­ies inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2] # storing dictionaries in a list

for alien in aliens:
    print(alien)

# ex. more realistic
aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print('\n')

for alien in aliens[:3]: # modify first three aliens
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
    
    elif alien['color'] == 'yellow':
        alien['color'] = 'purple'
        alien['points'] = 240
        alien['speed'] = 'fast'

for alien in aliens[:5]: # print first 5 alien dictionaries
    print(alien)
print('...')
print(f"Total number of aliends: {len(aliens)}")


# A list in a dictionary
pizza = {
    'crust': 'thick',
    'toppings': ['mushroom', 'extra chees'],
}

print(f"You ordered a {pizza['crust']}-crust pizza "\
    "with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# more ex.
favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print('\t', language.title())


# A dictionary in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
            },
    
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
            }, 
        }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = f"{user_info['location']}"

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location}")
