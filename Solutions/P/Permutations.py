import unittest
from typing import List

from Tags import *

"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""


class Solution(object):
    def getTags(self):
        tags = [Difficulty.Medium, Topic.BackTracking]
        return tags

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            unused = nums[:i] + nums[i + 1:]
            allPermutations = self.permute(unused)

            res += [[nums[i]] + p for p in allPermutations]

        return res


class test_permutations(unittest.TestCase):
    def test_1(self):
        self.assertListEqual(sorted([[1]]), sorted(Solution().permute([1])))
        self.assertListEqual(sorted([[0, 1], [1, 0]]), sorted(Solution().permute([0, 1])))
        self.assertListEqual(sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
                             sorted(Solution().permute([1, 2, 3])))
