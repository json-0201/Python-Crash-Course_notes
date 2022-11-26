# 3-4. Guest List
guests = ['Elon Musk', 'Adolf Hitler', 'Mr.V', 'Bruce Lee']
for i in range(len(guests)):
    
    message = f'Dear {guests[i]}, would you like to come to my dinner tomorrow?'
    print (message)

# 3-5. Changing Guest List
cannot_come = 'Adolf Hitler'
print('\n'f'{cannot_come.title()} cannot make it to the dinner.')

new_guest1 = 'Joesph Stalin'
guests[1] = new_guest1
print('\n'f"I will invite {new_guest1} to replace {cannot_come}'s spot.")

for i in range(len(guests)):

    message = f'Dear {guests[i]}, would you like to come to my dinner tomorrow?'
    print (message)

# 3-6. More Guests
new_guest2, new_guest3, new_guest4 = 'Naruto', 'Mikasa', 'Goku'
print('\n'f'I have found a bigger table, so I am also inviting {new_guest2}, {new_guest3} and {new_guest4}')

guests.insert(4, new_guest2)
guests.insert(5, new_guest3)
guests.append(new_guest4)

for i in range(len(guests)):

    message = f'Dear {guests[i]}, would you like to come to my dinner tomorrow?'
    print(message)

# 3-7. Shrinking Guest List
print('\n'"The table won't arrive in time - I have space for two guests. Damn it!")

for i in range(len(guests)):
    
    guests.pop()

    if len(guests) == 2:
       
        break

for i in range(len(guests)):

    message = f'Dear {guests[i]}, you are still invited to my dinner tomorrow.'
    print(message)

print(f'My guests are {guests}')


print('\nActually, I do not want to have anyone for dinner.')
del guests[0]
del guests[0]

print(f'My guests are: {guests}')
