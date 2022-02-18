class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        if len(nums) == 2:
            if nums[0] > nums[1]:
                return 0
            return 1
        """
        if len(nums) == 1:
            return 0

        start = 0
        size = end = len(nums)
        mid = 0
        while start < end:
            mid = (start+end)//2
            if mid == 0:
                if nums[0] > nums[1]:
                    return 0
                return 1
            if mid == size - 1:
                if nums[size - 1] > nums[size - 2]:
                    return size-1
                return size - 2

            if nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid

            #f'[mid] > 0 ===> going right
            if nums[mid] < nums[mid+1] and nums[mid-1] < nums[mid]:
                start = mid + 1
            else:
                end = mid

        return mid