"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        if nums[0] == target:
            return 0

        if len(nums) == 1:
            return -1

        jump = self.__findJump(nums)
        index = self.__binarySearch(nums[:jump],target)
        if index > -1:
            return index
        index =  self.__binarySearch(nums[jump:],target)
        if index > -1:
            return index+jump

        return -1

    def __findJump(self,nums):
        s = 0
        e = len(nums)

        while s<e:
            mid = (s+e)//2

            if mid == 0:
                return 1

            if nums[mid] < nums[mid-1]:
                return mid

            if nums[mid] < nums[0]:
                e = mid
            else:
                s = mid+1

        return s

    def __binarySearch(self, nums, target):
        s = 0
        e = len(nums)

        while s < e:
            mid = (s + e) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                e = mid
            else:
                s = mid + 1

        return -1

sol = Solution()
arr = [1,3]
target = 3
print(sol.search(arr, target))