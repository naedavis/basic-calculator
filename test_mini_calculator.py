import unittest


#basic structure needed before writing a test
from main import Add


class TestAdd(unittest.TestCase):

    def test_add(self):
        #only the instance of this class can access this
        a_method = Add()
        #wanna check if our add is going to add
        #needs 1st and second parameter and message when test failed
        #a_method inserted so we want to access the add method
        self.assertEqual(2, a_method.add(1,1)," adding 1 to 1 equal 2")

#in terminal python3 -m unittest test_mini_calculator