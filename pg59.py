# List Comprehensions = combines the for loop and the creation of new elements
squares = [value ** 2 for value in range(1,11)]
print(squares)

# 4-3. Counting to Twenty
for i in range(1,21):
    print(i)

# 4-4. One Million
'''
for i in range(1, 1_000_001):
    print(i)
'''

# 4-5. Summing a Million
numbers = [i for i in range(1, 1_000_001)]

print(min(numbers))
print(max(numbers))
print(sum(numbers))

# 4-6. Odd Numbers
odd_numbers = [i for i in range(1,20,2)]
print(odd_numbers)

# 4-7. Threes
threes = [i for i in range(3,31,3)]
print(threes)

# 4-8. Cubes
cubes = []

for i in range(1,11):
    cubes.append(i**3)

print(cubes)

# 4-9. Cubes, list comprehension
cubes = [i**3 for i in range(1,11)]
print(cubes)
