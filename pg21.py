# using variables in string

first_name = 'jimmy'
last_name = 'son'

# f-string: place 'f' before the opening quotation mark
# use brackets {} for strings
# space between brackets when necessary

full_name = f'{first_name} {last_name}'
print(full_name)

# assign f-string to a variable
greeting = f'Hello, {full_name.title()}'
print(greeting)