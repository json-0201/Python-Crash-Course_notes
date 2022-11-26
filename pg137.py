# Return values
# The return statement takes a value from inside a function and sends it back to the line that called the function

from numpy import full


def get_formatted_name(first_name, last_name):
    '''return a full name, neatly formatted'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()

my_name = get_formatted_name('jimmy', 'son')
print(my_name)

# making an argument optional
# add a default, empty string

def get_formatted_name(first_name, last_name, middle_name =''):
    '''return a full name, neatly formatted'''
    if middle_name:     # non-empty string = True
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

my_name = get_formatted_name('jimmy', 'son', middle_name = 'jam')
print(my_name)

# returning a dictionary
def build_person(first_name, last_name):
    '''return a dictionary of information about a person'''
    person = {'first': first_name.title(), 'last': last_name.title()}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# ex.
def build_person(first_name, last_name, age = None):    # None - variable has no specific value assigned to it (In conditional tests, None evaluates to False)
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age = 28)    #
print(musician)

# using a function with a while loop
def get_formatted_name(first_name, last_name):
    '''return a full name, neatly formatted'''
    full_name = f'{first_name} {last_name}'
    return full_name.title()

# infinite loop
while True:
    print('\nPlease tell me your name:')
    print('Please enter \'q\' to quit.')
    
    f_name = input('First name: ')
    if f_name == 'q':
        break
    l_name = input('Last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}!')

# 8-6. City Names
def city_country(city, country):
    formatted = f'{city}, {country}'
    return formatted.title()

cc1, cc2, cc3 = city_country('madrid', 'spain'), city_country('daegu', 'south korea'), city_country('riverside', 'united states')
ccs = [cc1, cc2, cc3]
print('\n')
for cc in ccs:
    print(cc)

# 8-7. Album
def make_album(artist_name, album_title, num_tracks = None):    # without None, python expects 3 arguments - 2 arguments will return an error
    '''returns a dictionary containing artist and album title information'''
    album = {}
    album['artist name'] = artist_name
    album['album title'] = album_title
    if num_tracks:
        album['number of tracks'] = num_tracks
    return album

album_1 = make_album('The Notorious B.I.G', 'Born  Again (1999)', 18)
print('\n', album_1)

# 8-8. User Albums
def make_album(artist_name, album_title, num_tracks = None):    # without None, python expects 3 arguments - 2 arguments will return an error
    '''returns a dictionary containing artist and album title information'''
    album = {}
    album['artist name'] = artist_name
    album['album title'] = album_title
    if num_tracks:
        album['number of tracks'] = num_tracks
    return album

while True:
    art_name = input('\nEnter the name of artist:\
        \n(Enter \'q\' to exit.)\n\tresponse:')
    if art_name == 'q':
        break
    alb_title = input('\nEnter the name of album:\
        \n(Enter \'q\' to exit.)\n\tresponse:')
    if alb_title == 'q':
        break
    nums = input('\nEnter the number of tracks:\
        \nHit \'Enter\' if unknown.\
        \n(Enter \'q\' to exit.)\n\treponse:')
    if nums == 'q':
        break

    album_info = make_album(art_name.title(), alb_title.title(), nums)
    print('\nalbum information: ', album_info)
