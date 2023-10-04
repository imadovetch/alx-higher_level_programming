#!/usr/bin/python3
"""Unittest define func for the max_integer"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """class that has many function which test many cases"""
    def test_with_int(self):
        """avarage test with integers: should return the max value"""
        list = [1, 2, 5, 200]
        output = max_integer(list)
        self.assertEqual(output, 200)

    def test_with_float(self):
        """test with float digits: return the max value"""
        list = [0.4, 50.7, 51.9]
        output = max_integer(list)
        self.assertEqual(output, 51.9)

    def test_with_string(self):
        """test with string and it should return typeerror"""
        list = ['a', 'b', 1]
        self.assertRaises(TypeError, max_integer, list)

    def test_it_empty(self):
        """test the func with empty data: return valueerror"""
        list = []
        output = max_integer(list)
        self.assertEqual(output, None)

    def test_as_not_list(self):
        """test it as normal variable: return TypError"""
        list = 9
        self.assertRaises(TypeError, max_integer, list)

    def test_as_unique(self):
        """test with unique value: retunr itself"""
        list = [23]
        output = max_integer(list)
        self.assertEqual(output, 23)

    def test_with_same_value(self):
        """test with same data: return that data"""
        list = [9, 9, 9]
        output = max_integer(list)
        self.assertEqual(output, 9)

    def test_with_none(self):
        """test with none data: return none"""
        self.assertRaises(TypeError, max_integer, None)

    def string_test(self):
        """return 1st string"""
        list = ['man', 'woman']
        output = max_integer(list)
        self.assertEqual(output, 'man')

if __name__ == '__main__':
    unittest.main()
