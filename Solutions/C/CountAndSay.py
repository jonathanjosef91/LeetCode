import unittest
from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""

class Solution(object):
    def getTags(self):
        tags = [Difficulty.Beginners, Topic.Strings]
        return tags

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        previousSay = self.countAndSay(n-1)
        currentSay = ""

        counter = 0
        savedChar = previousSay[0]

        for c in previousSay:
            if savedChar == c:
                counter += 1
            else:
                currentSay += (str(counter)+savedChar)
                savedChar = c
                counter = 1

        currentSay += (str(counter) + savedChar)
        return currentSay


class test_countAndSay(unittest.TestCase):
    def test_1(self):
        self.assertEqual("1", Solution().countAndSay(1))
        self.assertEqual("1211", Solution().countAndSay(4))
        self.assertEqual("111221", Solution().countAndSay(5))
