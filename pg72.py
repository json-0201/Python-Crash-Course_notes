# IF statements
# A simple example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    
    if car == 'bmw':

        print(car.upper())
    
    else:
        
        print(car.title())


# Conditional Tests - True / False
if True:
    print('Python executes if True')

if False:
    print('Python doesn\'t execute if False')


# Checking for equality, == equality operator - returns True/False
car = 'KIA'
car == 'KIA'
print('\n', car == 'KIA')
print('\n', car == 'BMW')


# equality check is case-sensitive
car = 'KIA'
car == 'KIA'
print('\n', car == 'Kia')
print('\n', car.lower() == 'kia')


# Checking for inequality, != inequality operator
requested_topping = 'mushrooms'

if requested_topping != 'anchovies':

    print('don\'t add anchovies!'.upper())


# Numerical comparisons, ==, !=, <, <=, >, >=
age = 18
print(age == 18)

answer = 21
if age != 42:
    print('Incorrect answer, please try again!\n')


# Checking multiple conditions using - 'and', 'or'
age_0 = 22
age_1 = 18
var_condition = age_0 != age_1 # assign condition to variable
print((age_0 != 13) and (age_1 <= 30)) # add () for readability
print((age_0 != 13) and (age_1 >= 30))
print('\nvar_condition\n')

print((age_0 != 13) or (age_1 <= 30))
print((age_0 != 13) or (age_1 >= 30))
