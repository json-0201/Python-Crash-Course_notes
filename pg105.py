# 6-4. Glossary 2
languages = {
    'python': 'what I am learning now',
    'ruby': 'I think it\'s for back end programming',
    'c++': 'I hated this class in college',
    'java': 'I studied it shortly in the past',
    'c': 'I have no clue, I guess it\'s similar to c++?',
    'python_': 'i will become a python programmer!',
}

for language, sentence in languages.items():
    print(f"{language.title()}: {sentence.title()}.")


# 6-5. Rivers
rivers = {
    'nile': 'egypt',
    'amazon': 'brasil',
    'yangtze': 'china',
    'missouri': 'USA',
    'han': 'korea', 
}

print('\n')
for river, country in rivers.items():
    print(f"{river.title()} runs through {country.title()}.")

for river in rivers.keys():
    print(f"{river.title()}")
for country in rivers.values():
    print(f"{country.title()}")


# 6-6. Polling
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

names = ['sarah', 'john', 'nick', 'pablo', 'phil']
print('\n')
for name in names:
    if name in favorite_languages.keys():
        print(f"{name.title()}, thank you for taking the poll!")
    
    else:
        print(f"{name.title()}, please take our poll!")
