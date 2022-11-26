# Testing the AnonymousSurvey Class
import unittest
from survey import AnonymousSurvey  # import class from module

class TestAnonymousSurvey(unittest.TestCase):
    '''tests for the class AnonymousSurvey'''

    def test_store_single_response(self):
        '''test that a single response is stored properly'''
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)   # instance of class AnonymousSurvey
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)   # assertIn to check the item in the list
                                                        # access the list by instance.attribute (my_survey.responses)

    def test_store_three_responses(self):
        '''test that three individual responses are stored properly'''
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['Korean', 'English', 'Spanish']
        for response in responses:
            my_survey.store_response(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)

if __name__ == '__main__':
    unittest.main()

# This works perfectly. However, these tests are a bit repetitive, so we’ll use another feature of unittest to make them more efficient