# User input and while loops
# input()
# while loop to keep the program running

message = input('tell me something, and I will repeat it bakc to you: ') # the response is assigned to the variable message
print(message.upper(), '\n')

# ex.
name = input('Please enter your name: ')
print(f"\nHello, {name.title()}!")

# ex.
prompt = 'If you tell us who you are, we can personalize the message you see.'
prompt += '\nWhat is your name? '

name = input(prompt)
print(f'Your name is {name.title()}!')

# python interprets user input as a string
# needs int() to convert the input
age = input('How old are you? ')
print(age) # age is in string

# if age >= 10: # gives error
age = int(age)
if age >= 10:
    print('You can enter this zoo.')

# ex.
height = input('How tall are you, in inches? ')
height = int(height)

if height >= 48:
    print('\nYou are tall enough to ride.')
else:
    print('\nYou will be able to ride when you\'re a little older!')

