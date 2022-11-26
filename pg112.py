# 6-7. People
from sklearn.metrics import precision_recall_fscore_support


person_1 = {'first name': 'Jimmy', 'last name': 'Son', 'age': 28, 'city': 'Madrid',}
person_2 = {'first name': 'Maria', 'last name': 'Cano', 'age': 24, 'city': 'Bilbao',}

people = [person_1, person_2]

for person in people:
    print(person, '\n')

# 6-8. Pets
pet_1 = {'type': 'dog', 'owner': 'sara'}
pet_2 = {'type': 'cat', 'owner': 'eva'}
pet_3 = {'type': 'lion', 'owner': 'john'}
pet_4 = {'type': 'parrot', 'owner': 'pablo'}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(pet, '\n')

# 6-9. Favorite places
favorite_places = {
    'pedro': ['london', 'madrid', 'paris'],
    'james': ['sidney', 'new york', 'riverside'],
    'jose': ['oslo', 'los angeles', 'mexico city'],
    }

for name, place in favorite_places.items():
    if len(place) == 1:
        print(f"{name.title()}'s favorite place is {place[0].title()}.")    
    else:
        print(f"{name.title()}'s favorite places are {place[0].title()}, {place[1].title()} and {place[2].title()}.")

print('\n')

# 6-10. Favorite numbers
favorite_numbers = {
    'john': [5, 6],
    'daniel': [7, 9],
    'sam': [10, 4, 13],
    'rachael': [13],
}

for name, numbers in favorite_numbers.items():
    if len(str(numbers)) == 1:
        print(f"{name.title()}'s favorite number is:")
        print(f"\t{numbers}.")
    else:
        print(f"{name.title()}'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}.")
print('\n')

# 6-11. Cities
city_1 = {'country': 'united states', 'population': '3.9m', 'fact': 'This city is expensive to live!'}
city_2 = {'country': 'spain', 'population': '3.2m', 'fact': 'You can hear so many languages in this city!'}
city_3 = {'country': 'norway', 'population': '0.63m', 'fact': 'This city makes me feel calm'}

cities = {
    'los angeles': city_1,
    'madrid': city_2,
    'oslo': city_3,
}

for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"\tCountry: {info}")

# 6-12. Extensions
###
