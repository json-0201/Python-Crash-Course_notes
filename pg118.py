# while Loops - runs as long as/while a certain condition is True
# while loop in action
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# letting the user choose when to quit
prompt = '\nTell me something, and I will repeat it back to you.'
prompt += '\n[Enter \'quit\' to end the program.]'
prompt += '\ninput:'

message = '' # first while loop run check

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

# using a flag
# flag acts as a signal to the program
# cleans and organizes the program
prompt = '\nTell me something, and I will repeat it back to you.'
prompt += '\n[Enter \'quit\' to end the program.]'
prompt += '\ninput:'

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# using break to exit a loop
prompt = '\nPlease enter the name of a city you have visited:'
prompt += '\n[Enter \'quit\' when you are finished.]'

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f'You have been to {city.title()}.')

# using continue in a loop
current_number = 0
while current_number <= 10:
    current_number += 1
    if current_number % 2 == 0:
        continue                # even number will ignore the rest of the loop and return to the beginning
    
    print(current_number)

# avoiding infinite loops
# make sure at least one part of the program can make the loop’s condition False or cause it to reach a break statement

# 7-4. Pizza Toppings
active = True
while active:
    topping = input('\nWhich topping would you like to add to your pizza?:')
    if topping == 'quit':
        active = False
    if topping != 'quit':
        print(f'\n\t{topping} has been added to your pizza.')

# 7-5, 7-6. Movie Tickets
number_people = 8
index = 0
while index < number_people:
    age = input('\nWhat is your age?\n\t[Enter \'quit\' to exit the program.]\nEnter your age:')
    
    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print('Your ticket is free.')
    elif age < 12:
        print('Your ticket is $10.')
    else:
        print('Your ticket is $15.')
    
    index += 1

# 7-7 Infinity
while True:
    print('This is an infinite loop. HA!')
