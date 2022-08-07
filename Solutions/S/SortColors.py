import unittest
from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""

class Solution(object):
    def getTags(self):
        tags = [Difficulty.Beginners, Topic.Sorting] # TODO: Change
        return tags

    def sortColors_hist(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Results:
        Runtime: 22 ms
        Memory Usage: 13.6 MB
        """
        if len(nums) == 0:
            return

        hist = [0, 0, 0]
        for num in nums:
            hist[num] += 1

        # n = 0
        # for i in range(len(hist)):
        #     for j in range(hist[i]):
        #         nums[n] = i
        #         n += 1

        for i in range(len(nums)):
            if i < hist[0]:
                nums[i] = 0
            elif i < hist[0] + hist[1]:
                nums[i] = 1
            else:
                nums[i] = 2

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Results:
        Runtime: 23 ms
        Memory Usage: 13.3 MB
        """
        if len(nums) == 0:
            return

        l = 0
        i = 0
        r = len(nums) - 1

        while nums[r] == 2 and r >= i:
            r -= 1

        while i <= r:

            if nums[i] == 0:
                if i > l:
                    l, i = self._swapLeft(nums, l, i, r)
                else:
                    i += 1
                    l += 1
            elif nums[i] == 1:
                i += 1
            else:
                i, r = self._swapRight(nums, i, r)

    def _swapRight(self, nums, i, r):
        tmp = nums[r]
        nums[r] = nums[i]
        nums[i] = tmp

        r -= 1
        while nums[r] == 2 and r >= i:
            r -= 1

        return i, r

    def _swapLeft(self, nums, l, i, r):
        tmp = nums[l]
        nums[l] = nums[i]
        nums[i] = tmp

        l += 1
        while (nums[i] == 0 and i <= r):
            i += 1

        return l, i


class test_sortColors(unittest.TestCase):
    def test_hist(self):
        nums = [2, 0, 2, 1, 1, 0]
        Solution().sortColors_hist(nums)
        self.assertEqual([0,0,1,1,2,2], nums)

        nums = [2,0,1]
        Solution().sortColors_hist(nums)
        self.assertEqual([0, 1, 2], nums)

    def test_1(self):
        nums = [2, 0, 2, 1, 1, 0]
        Solution().sortColors(nums)
        self.assertEqual([0,0,1,1,2,2], nums)

    def test_2(self):
        nums = [2,0,1]
        Solution().sortColors(nums)
        self.assertEqual([0, 1, 2], nums)

    def test_3(self):
        nums = [0,0]
        Solution().sortColors(nums)
        self.assertEqual([0, 0], nums)

    def test_4(self):
        nums = [2,2]
        Solution().sortColors(nums)
        self.assertEqual([2, 2], nums)

    def test_5(self):
        nums = [1, 0]
        Solution().sortColors(nums)
        self.assertEqual([0, 1], nums)

    def test_6(self):
        nums = [1, 2, 0]
        Solution().sortColors(nums)
        self.assertEqual([0, 1, 2], nums)