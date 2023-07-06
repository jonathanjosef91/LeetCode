import unittest
from typing import List

from Tags import *

"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""


class Solution(object):
    def getTags(self):
        tags = [Difficulty.Beginners, Topic.DP]
        return tags

    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        values = []

        for i in range(len(nums)):
            m = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    m = max(values[j] + 1, m)
            values.append(m)

        return max(values)


class test_lengthOfLIS(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
        self.assertEqual(4, Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]))
        self.assertEqual(1, Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))
