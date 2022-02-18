import unittest
from Tags import Tags
"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""

class Solution(object):
    def getTags(self):
        tags = [Tags.Beginners, Tags.Strings] # TODO: Change
        return tags

    def template(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s


class test_template(unittest.TestCase):
    def test_1(self):
        self.assertEqual("test", Solution().template("test"))
        self.assertIn("test", [Solution().template("test")])
        self.assertGreaterEqual(3, int(Solution().template("2")))
