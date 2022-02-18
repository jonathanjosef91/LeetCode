import unittest
from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""

class Solution(object):
    def getTags(self):
        tags = [Difficulty.Hard, Topic.DP, Topic.Strings]
        return tags

    def longestPalindrome(self, s):
        if s == "":
            return ""
        isPali = [[False] * len(s) for i in range(len(s))]
        max_pali = s[0]
        max_l = 1

        for i in range(len(s)):
            isPali[i][i] = True

        for j in range(1, len(s)):
            for i in range(j - 1, -1, -1):
                isPali[i][j] = (isPali[i + 1][j - 1] or j - i < 2) and s[i] == s[j]
                if isPali[i][j]:
                    if j - i + 1 > max_l:
                        max_l = j - i
                        max_pali = s[i:j + 1]

        return max_pali

class test_longestPalindrome(unittest.TestCase):
    def test_1(self):
        res = Solution().longestPalindrome("babad")
        self.assertTrue(res in ["bab", "aba"])
        self.assertEqual("bb", Solution().longestPalindrome("cbbd"))
        self.assertEqual("bb", Solution().longestPalindrome("bb"))
        self.assertEqual("ccc", Solution().longestPalindrome("ccc"))
        self.assertEqual("aca", Solution().longestPalindrome("aacabdkacaa"))
