# Looping through a dictionary
# lopping through all key-value pairs
## for key, value in dictionary.items()
user_0 ={
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

print(user_0.items())

for key, value in user_0.items():
    print(f"\nKey: {key.title()}")
    print(f"Value: {value.title()}")

# ex.
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {favorite_languages[name].title()}.")
    print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through all the keys in a dictionary
# default behavior
## keys()
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print('\n')
for name in favorite_languages.keys(): # add .keys() for readability
    print(name.title())

print('\n')
for name in favorite_languages:
    print(name.title())

# ex. - check for key list
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

friends = ['phil', 'sarah', 'erin']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        langauge = favorite_languages[name].title()
        print(f"\tHi {name.title()}, I see you love {language.title()}!")
    
if 'erin' not in favorite_languages.keys():
    print('\n\tErin, please take our poll!')

# looping through a dictionary's keys in a particular order
# use sorted() function to get a copy of the keys in order
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking our poll!")

# looping through all values in a dictionary
# .values()
favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

print('\nThe following lamguages have been mentioned:')
for language in favorite_languages.values():
    print(f'\t{language.title()}')

# set - a collection in which each item must be unique
# set - braces without key-value pairs
# set - to see each value without repetition
print(set(favorite_languages.values()))

print('\nThe following lamguages have been mentioned:')
for language in set(favorite_languages.values()):
    print(f'\t{language.title()}')

# manually create a set
languages = {'python', 'ruby', 'python', 'c'}
print(languages) # return elements without repetition
