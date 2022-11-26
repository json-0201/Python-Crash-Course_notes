from pg180_user import User

class Admin(User):
    '''creating child class from parent class User'''
    
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        print(f'List of administrator\'s privileges: {self.privileges}')
        