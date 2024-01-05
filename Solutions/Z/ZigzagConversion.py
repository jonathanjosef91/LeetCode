import unittest
from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""

class Solution(object):
    def getTags(self):
        tags = [Difficulty.Hard, Topic.Strings]
        return tags

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        res = ''
        delta = (2*(numRows-1))

        for r in range(numRows):
            if r == 0 or r == numRows - 1:
                i = r
                while i < len(s):
                    res += s[i]
                    i += delta

            else:
                indices = [r, delta-r]
                i = 0
                while indices[i] < len(s):
                    res += s[indices[i]]
                    indices[i] += delta
                    i = ((i+1) % len(indices))

        return res



class test_zigzagConversion(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(Solution().convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(Solution().convert("PAYPALISHIRING", 1), "PAYPALISHIRING")
        self.assertEqual(Solution().convert("ABCD", 3), "ABDC")
        self.assertEqual(Solution().convert("a", 7), "a")
