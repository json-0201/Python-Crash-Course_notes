# 11-3. Employee
import unittest
class Employee:
    def __init__(self, first, last, salary):
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def give_raise(self, amount = 5000):
        self.prev_salary = self.salary
        self.salary += amount
        print(f'{self.first_name.title()} {self.last_name.title()}\'s current salary: {self.prev_salary}')
        print(f'{self.first_name.title()} {self.last_name.title()}\'s new salary: {self.salary}\n')

class TestSalaryRaise(unittest.TestCase):
    '''test give_raise method in class Employee'''

    def setUp(self):
        self.employee_1 = Employee('Jimmy', 'Son', 75000)

    def test_default_raise(self):
        self.employee_1.give_raise()
        self.assertEqual(self.employee_1.salary, self.employee_1.prev_salary+5000)

    def test_custom_raise(self):
        self.employee_1.give_raise(20000)
        self.assertEqual(self.employee_1.salary, self.employee_1.prev_salary+20000)

if __name__ == '__main__':
    unittest.main()
