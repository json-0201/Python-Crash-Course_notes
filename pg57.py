# Making numerical lists
for i in range (0,5):
    print(i)

print('\n')

for i in range (1,5):
    print(i)

# list() function to convert range() to a list
numbers = list(range(1,11))
print(numbers)

# range(a,b,c) - a: start, b: end, c: step
even_numbers = list(range(2,11,2))
print(even_numbers)

odd_numbers = list(range(1,10,2))
print(odd_numbers)

squares = []
for i in range(1,11):
    
    # square = i*i
    # i*i = i**2
    squares.append(i**2)

print(squares, '\n')

# min, max, sum
print(min(squares))
print(max(squares))
print(sum(squares))
