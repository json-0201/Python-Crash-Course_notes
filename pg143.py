# passing a list
from email import message


def greet_users(names):
    '''print a simple greeting to each user in the list'''
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)

usernames = ['jim_1', 'jim_2', 'jim_3', 'jim_4']
greet_users(usernames)

# modifying a list in a function
# divide the task in 2 or more functions
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'\nPrinting {current_design.title()}...\
            \n{current_design.title()} completed!')
        
        completed_models.append(current_design)
        print(f'{current_design.title()} has been added to the list of completed models.\n')
    
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print(f'\nThe following models have been printed:')
    for completed_model in completed_models:
        print('\t', completed_model.title())

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)

### every function should have one specific job ###
### If you’re writing a function and notice the function is doing too many different tasks, try to split the code into two functions. ###

# preventing a function from modifying a list
# making a copy of the original list before the list becomes empty
# function_name(list_name[:]) / list_name.copy()

# ex.
print_models(unprinted_designs.copy(), completed_models) # list_name[:] or list_name.copy() ---> copy of a list
show_completed_models(completed_models)
print(unprinted_designs) # still contains original values

# 8-9. Messages
messages = ['salveee migo', 'yo what up D?', 'hola que tal bro']
def show_messages(messages):
    for message in messages:
        print(message.upper())

print('\n')
show_messages(messages)

'''

# 8-10. Sending Messages
print('\n')
messages = ['salveee migo', 'yo what up D?', 'hola que tal bro']
sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f'{current_message.upper()}')
        sent_messages.append(current_message)

send_messages(messages, sent_messages)

print(messages)
print(sent_messages)

'''

# 8-11. Archived Messages
print('\n')
messages = ['salveee migo', 'yo what up D?', 'hola que tal bro']
sent_messages = []

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f'{current_message.upper()}')
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages) # input list as a copy

print('\n', sorted(messages))
print('\n', sorted(sent_messages))
