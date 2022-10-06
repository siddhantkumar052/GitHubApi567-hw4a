import unittest

from getRepo import getRepo

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestGithubAPI(unittest.TestCase):
    def testGithub1(self):
        self.assertEqual(getRepo('siddhantkumar052'), True)
       
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()