import unittest
from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""


def createdict(nums):
    numsMap = dict.fromkeys(nums)
    for i in numsMap:
        numsMap[i] = 0
    for i in range(0, len(nums)):
        numsMap[nums[i]] += 1
    return numsMap


def removeDuplicate(nums):
    temp = []
    for i in nums:
        if i not in temp:
            temp.append(i[:])
    return temp


class Solution(object):
    def getTags(self):
        tags = [Difficulty.Beginners, Topic.Searches, Tags.Old]
        return tags

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            numsMap = createdict(nums[i + 1:])
            for j in range(i + 1, len(nums) - 1):
                numsMap[nums[j]] -= 1
                reminder = (-1) * (nums[i] + nums[j])
                if reminder in numsMap and numsMap[reminder] > 0:
                    temp = [nums[i], nums[j], reminder]
                    temp.sort()
                    rList.append(list(temp))
        rList = removeDuplicate(rList)

        return rList

class Test_3sum(unittest.TestCase):
    def test_1(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum([-1, 0, 1, 2, -1, -4]))
