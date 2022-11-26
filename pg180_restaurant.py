class Restaurant:
    '''a simple attempt to model a restaurant'''

    def __init__(self, name, cuisine_type):
        '''initialize name and cuisine type attributes'''
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        '''prints the name and cuisine type of a restaurant'''
        print(f'\nThe restaurant is called {self.name.title()} and it serves {self.cuisine_type.title()} food.')
    
    def open_restaurant(self):
        '''prints that the restaurant is open'''
        print(f'{self.name.title()} is open now.')
        