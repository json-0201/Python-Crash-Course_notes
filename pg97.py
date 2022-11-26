# A dictionary of similar objects
# dictionary can be broken into multiple lines
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print(f"\nPhil's favorite language is {favorite_languages['phil'].title()}")

# get() to access values - get('value', 'return')
alien_0 = {'color': 'green', 'speed': 'slow'}
print('Alien color is ' + alien_0.get('color'))

# get() to set a default value to be returned if key doesn't exist
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
