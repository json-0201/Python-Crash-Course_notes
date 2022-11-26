# Dictionaries: key-value pairs, {}
# A simple dictionary - key: value
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color']) # access value by key
print(alien_0['points']) # access value by key

# Assign value of dictionary to variable
new_points = alien_0['points']
print(f'\nYou have just earned {new_points} points!')

# Adding new key-value pairs
alien_0 = {'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print('\n', alien_0)

# Starting with an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5
print('\n', alien_0)

# Modifying values in a dictionary
alien_0 = {'color': 'green', 'points': 5}
print(f"\nThe alien is {alien_0['color']}")
alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}")
################################################################################
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"\nOriginal position: {alien_0['x_position']}")

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

# Removing key-value pairs
# del statement
alien_0 = {'color': 'green', 'points': 5}
print('\n', alien_0)

del alien_0['points'] # use key to remove key-value pair
print(alien_0)
