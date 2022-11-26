# The Modulo Operator, % - returns remainder
number = input('Enter a number, and I\'ll tell you if it is even or odd: ')
number = int(number)

if number % 2 == 0:
    print(f'The number {number} is even.')
else:
    print(f'The number {number} is odd.')

# 7-1. Rental Car
car = input('What type of car do you need? ')
print(f"Hold on, I will see if we have any available {car}.")

# 7-2. Restaurant Seating
people = input('How many people are in your group? ')
people = int(people)

if people > 8:
    print('You guys will have to wait for a table.')
else:
    print('Your table is ready. Follow me.')

# 7-3. Multiples of Ten
number = input('Enter a number, and I\'ll tell you if it is a multiple of ten: ')
number = int(number)

if number % 10 == 0:
    print(f'The number {number} is a multiple of ten.')
else:
    print(f'The number {number} is not a multiple of ten.')
