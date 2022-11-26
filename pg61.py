# Working with part of a list

# slicing a list - a:b returns index from 'a' to 'b-1'
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3], '\n')

print(players[0:4])
print(players[:4]) # Python automatically starts slicing at the beginning of the list

print(players[1:]) # Python automatically ends slicing at the end of the list

# slicing last 3 index
print(players[-3:])

# stepping while slicing a list
numbers = [i for i in range(1, 101)]
print(numbers[0:100:5])

# looping through a slice
print('\nHere are the first three players on my team:')
for player in players[:3]:
    print(player.title())
