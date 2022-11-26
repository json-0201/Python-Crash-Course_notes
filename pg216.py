# Testing a Class
'''
You’ll use classes in many of your own programs, so it’s helpful to be able to prove that your classes work correctly.
If you have passing tests for a class you’re working on,
you can be confident that improve ments you make to the class won’t accidentally break its current behavior.
'''

# Python provides a number of assert methods in the unittest.TestCase class

#assertEqual(a, b) --- Verify that a == b
#assertNotEqual(a, b) --- Verify that a != b
#assertTrue(x) --- Verify that x is True
#assertFalse(x) --- Verify that x is False
#assertIn(item, list) --- Verify that item is in list
#assertNotIn(item, list) --- Verify that item is not in list

# a class to test
class AnonymousSurvey:  # saved as survey.py in the directory
    '''collect anonymous answers to a survey question'''

    def __init__(self, question):
        '''store a question and prepare to store responses'''
        self.question = question
        self.responses = []
    
    def show_question(self):
        '''show the survey question'''
        print(self.question)

    def store_response(self, new_response):
        '''store a single response to the survey'''
        self.responses.append(new_response)

    def show_results(self):
        '''show all the responses that have been given'''
        print('survey results: ')
        for response in self.responses:
            print(f'\t- {response}')

from survey import AnonymousSurvey

# define a question, and make a survey
question = 'what language did you first learn to speak?'
my_survey = AnonymousSurvey(question)   # instance of class AnonymousSurvey

# show the question, and store responses to the question
my_survey.show_question()
print('Enter \'q\' at any time to quit.\n')
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

# show the survey results
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()
