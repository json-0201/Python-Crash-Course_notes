# 6-1. Person
info = {'first name': 'Jimmy', 'last name': 'Son', 'age': 28, 'city': 'Madrid',}
for key in info:
    print(f'{key}: {info[key]}')

# 6-2. Favorite Numbers
favorite_numbers = {
    'john': 5,
    'daniel': 7,
    'sam': 10,
    'rachael': 13,
}
for key in favorite_numbers:
    print(f'{key.title()}\'s favorite number is {favorite_numbers[key]}.')

# 6-3. Glossary
languages = {
    'python': 'what I am learning now',
    'ruby': 'I think it\'s for back end programming',
    'c++': 'I hated this class in college',
    'java': 'I studied it shortly in the past',
    'c': 'I have no clue, I guess it\'s similar to c++?',
}
for key in languages:
    print(f'\n{key.title()}: {languages[key]}.')
