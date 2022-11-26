# Testing Your Code
# Python's unittest module
'''
When you write a function or a class, you can also write tests for that code.
Testing proves that your code works as it’s supposed to in response to all the input types it’s designed to receive.
'''

# testing a function
def get_formatted_name(first, last):
    '''this function returns neatly formatted full name'''
    full_name = f'{first} {last}'
    return full_name.title()

print('Enter \'q\' at any time to quit.')
while True:
    first = input('\nEnter first name: ')
    if first == 'q':
        break
    last = input('Enter last name: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f'\tNeatly formatted name: {formatted_name}')

# unit tests and test cases
'''
A unit test verifies that one specific aspect of a function’s behavior is correct.
A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to.

A test case with full coverage includes a full range of unit tests covering all the possible ways you can use a function.
Achieving full coverage on a large project can be daunting.
It’s often good enough to write tests for your code’s critical behaviors and then aim for full coverage only if the project starts to see widespread use.
'''

# adding new tests
import unittest
from name_function_3 import get_formatted_name  # name_function_3 contains 'middle' argument

class NameTestCase(unittest.TestCase):
    '''tests for 'name_function_2.py'.'''

    def test_first_last_name(self):
        '''do names like 'Janis Joplin' work?'''
        formatted_name = get_formatted_name(first = 'janis', last = 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):  # adding another test
        '''do names like 'Wolfgang Amadeus Mozart' work?'''
        formatted_name = get_formatted_name(first = 'wolfgang', middle = 'amadeus', last = 'mozart')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

# The two dots on the first line of output tells that two tests passed
# The next line tells Python ran two tests and took less than 0.001 seconds to run
# The final 'OK' tells us that all unit tests in the test case passed