import unittest
from Tags import *

"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""


class Solution(object):
    def getTags(self):
        tags = [Difficulty.Extreme, Topic.Sorting]
        return tags

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 1

        ptr = 0
        junk = len(nums)

        while ptr < junk:
            if nums[ptr] == ptr + 1:
                ptr += 1
                continue

            if nums[ptr] <= 0 or nums[ptr] >= junk or nums[ptr] == nums[nums[ptr] - 1]:
                junk -= 1
                nums[ptr], nums[junk] = nums[junk], nums[ptr]
                continue

            temp = nums[nums[ptr] - 1]
            nums[nums[ptr] - 1] = nums[ptr]
            nums[ptr] = temp

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


class test_firstMissingPositive(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2, Solution().firstMissingPositive([3, 3, 1, 4, 0]))
        self.assertEqual(1, Solution().firstMissingPositive([3, -7, 2, 4, 0]))
        self.assertEqual(6, Solution().firstMissingPositive([1, 2, 3, 5, 4]))
        self.assertEqual(1, Solution().firstMissingPositive([-7]))
        self.assertEqual(1, Solution().firstMissingPositive([]))
        self.assertEqual(2, Solution().firstMissingPositive([1, 1, 1, 1, 1, 1, 1, 1]))
