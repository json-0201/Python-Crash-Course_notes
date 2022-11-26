# 11-1. City, Country
from city_function import formatted_city_country
import unittest

class NameTestCase(unittest.TestCase):
    '''tests for 'formatted_city_country.py.'''

    def test_city_country(self):
        formatted_name = formatted_city_country('seoul', 'south korea')
        self.assertEqual(formatted_name, 'Seoul, South Korea')

if __name__ == '__main__':
    unittest.main()