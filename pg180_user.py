class User:
    '''a simple attempt to model a user'''

    def __init__(self, first_name, last_name):
        '''initialize first name and last name attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        '''prints out user info'''
        print(f'\nfirst name: {self.first_name.title()}, last name: {self.last_name.title()}')
    
    def greet_user(self):
        '''simple greeting'''
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!')
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        