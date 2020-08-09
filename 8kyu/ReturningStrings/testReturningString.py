'''import unittest
from ReturningStrings import greet

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(greet('Ryan'), 'Hello, Ryan how are you doing today?')

if __name__ == '__main__':
   unittest.main()        
'''
from ReturningStrings import greet

def test_returningString():
    assert greet('Ryan') == 'Hello, Ryan how are you doing today?'