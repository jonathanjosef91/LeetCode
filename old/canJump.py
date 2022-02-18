class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = 1
        for i in range(len(nums)-1):
            counter -= 1
            counter = max(counter,nums[i])
            if counter <= 0:
                return False

        return True