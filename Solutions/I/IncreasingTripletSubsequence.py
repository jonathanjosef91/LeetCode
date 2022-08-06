import unittest
from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/781/
"""

class Solution(object):
    def getTags(self):
        tags = [Difficulty.Medium, Topic.Searches]
        return tags

    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False

        min_num = nums[0]
        sec_to_min = None

        for num in nums:
            if num in [min_num, sec_to_min]:
                continue

            if sec_to_min is None:
                if num < min_num:
                    min_num = num
                else:                       # num > min_num
                    sec_to_min = num

            else:
                if num > sec_to_min:
                    return True
                else:                       # num < sec_to_min
                    if num < min_num:       # num < min_num < sec_to_min
                        min_num = num
                    else:                   # min_num < num < sec_to_min:
                        sec_to_min = num

        return False

class test_increasingTripletSubsequence(unittest.TestCase):
    def test_1(self):
        self.assertEqual(True, Solution().increasingTriplet([1,2,3,4,5]))
        self.assertEqual(False, Solution().increasingTriplet([5,4,3,2,1]))
        self.assertEqual(True, Solution().increasingTriplet([2,1,5,0,4,6]))
