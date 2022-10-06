"""
Name: Siddhantkumar Maske
Cwid:20006862
Subject: SSW 567
HW 04a Homework 04a - Develop with the Perspective of the Tester in mind
"""

import unittest

from getRepo import getRepo


class TestGithubAPI(unittest.TestCase):
    def testGithub1(self):
        self.assertEqual(getRepo('siddhantkumar052'), True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
