# The setUp() method
'''
When you include a setUp() method in a TestCase class,
Python runs the setUp() method before running each method starting with test_.
Any objects created in the setUp() method are then available in each test method you write.
'''

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''tests for the class AnonymousSurvey'''
    
    def setUp(self):    # self-index is to allow the instances to be used in anywhere in the class
        '''
        create a survey and a set of responses for use in all test methods
        '''
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Korean', 'English', 'Spanish']
    
    def test_store_single_response(self):
        '''test that a single response is stored properly'''
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    def test_store_three_responses(self):
        '''test that three individual responses are stored properly'''
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

'''
When you’re testing your own classes, the setUp() method can make your test methods easier to write.
You make one set of instances and attributes in setUp() and then use these instances in all your test methods.
This is much easier than making a new set of instances and attributes in eachtest method.
'''