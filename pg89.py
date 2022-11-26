# 5-8. Hello Admin
usernames = ['abcd1234', 'random815', 'coffee420', 'admin', 'kebablover94', 'iphone13pro']
if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')


# 5-9. No Users
usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {user}, thank you for logging in again.')
else:
    print('\nWe need to find some users!\n')


# 5-10. Checking Usernames
current_users = ['abcd1234', 'random815', 'coffee420', 'admin', 'kebablover94', 'iphone13pro']
new_users = ['1234abcd', 'random815', 'coffee360', 'matcha99', 'kebablover94', 'iphoneSE']
if new_users:
    for user in new_users:
        if user in current_users:
            print(f'{user}: This username has already been used. Please try a different username.')
        else:
            print(f'{user}: This username is available.')
else:
    print('We need to find some uesrs!')


# 5-11. Ordinal Numbers
numbers = list(range(1,10))
#for number in numbers:
#   print(number)
if numbers:
    for number in numbers:
        if number == 1:
            ordinal = 'st'
        elif number == 2:
            ordinal = 'nd'
        elif number == 3:
            ordinal = 'rd'
        else:
            ordinal = 'th'
        print(f'{number}{ordinal}')
