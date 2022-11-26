def get_formatted_name(first, last, middle = ''):
    '''this function returns neatly formatted full name'''
    if middle:  # if 'middle' is not an empty string
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()