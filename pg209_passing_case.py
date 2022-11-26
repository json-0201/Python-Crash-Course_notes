# Testing Your Code
# Python's unittest module
'''
When you write a function or a class, you can also write tests for that code.
Testing proves that your code works as it’s supposed to in response to all the input types it’s designed to receive.
'''

# testing a function, manually
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

# a passing test
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):     # inheritance from the class unittest.TestCase
    '''tests for 'name_function.py'.'''

    def test_first_last_name(self): # method that tests one aspect of get_formatted_name() function
        '''do names like 'Janis Joplin' work?'''
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')    # assert methods verify if the result matches the expected value
                                                            # assertEqual(result, expected value)

'''
A special variable, __name__, is set when the program is executed.
If this file is being run as the main program, the value of __name__ is set to '__main__'.
In this case, we call unittest.main(), which runs the test case.
When a testing framework imports this file, the value of __name__ won’t be '__main__' and this block will not be executed.
'''

print('')
if __name__ == '__main__':
    unittest.main()
# The dot on the first line of output tells that a single test passed
# The next line tells Python ran one test and took less than 0.001 seconds to run
# The final 'OK' tells us that all unit tests in the test case passed