# 3-8. Seeing the World
locations = ['Thailand', 'Vietnam', 'Japan', 'Finland', 'Romania']
print(locations)

print(sorted(locations))
print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

# 3-9. Dinner Guests
guests = ['Elon Musk', 'Adolf Hitler', 'Mr.V', 'Bruce Lee']
cannot_come = 'Adolf Hitler'
new_guest1 = 'Joesph Stalin'
guests[1] = new_guest1
new_guest2, new_guest3, new_guest4 = 'Naruto', 'Mikasa', 'Goku'
guests.insert(4, new_guest2)
guests.insert(5, new_guest3)
guests.append(new_guest4)

num_guest = len(guests)
print(f'The number of people I am inviting to dinner is {num_guest}.')

# 3-10. Every Function
powermoves = ['windmill', 'baby mill', 'flare', 'air flare', 'headspin', 'halo', '1990s', '2000s', 'elbow spin']
print(f"I've been working on my {powermoves[2]}.")

for i in range(len(powermoves)):

    message = f'I want to learn how to do {powermoves[i].title()}!'
    print (message)

powermoves.append('swipes')
print(powermoves)

fruits =[]

fruits.append('strawberry')
fruits.append('banana')
fruits.append('kiwi')
fruits.append('apple')

fruits.insert(0, 'watermelon')
print(fruits)

del fruits[0]
print(fruits)

fruits.append('mango')
print(fruits)

popped_fruit = fruits.pop()
print(popped_fruit)
print(fruits)

fruits.remove('kiwi')
print(fruits)

too_soft = 'banana'
print('\n', f'{too_soft.title()} is too soft for me!')

print('\n', fruits)

fruits.sort()
print('sorted alphabetically: ' + str(fruits))
print('sorted alphabetically:', (fruits))
print(f'sorted alphabetically: {fruits}')

fruits.sort(reverse=True)
print(fruits)

print(sorted(fruits))
print(fruits)

fruits.reverse()
print(fruits)

list_len = len(fruits)
print(list_len)
