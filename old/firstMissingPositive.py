class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 1

        ptr = 0
        junk = len(nums)

        while ptr<junk:
            if nums[ptr] == ptr+1:
                ptr += 1
                continue

            if nums[ptr] <= 0 or nums[ptr] >= junk or nums[ptr] == nums[nums[ptr]-1]:
                junk -= 1
                nums[ptr], nums[junk] = nums[junk], nums[ptr]
                continue

            temp = nums[nums[ptr]-1]
            nums[nums[ptr]-1] = nums[ptr]
            nums[ptr] = temp

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1


        return len(nums)+1


sol = Solution()
arr = [3,3,1,4,0]
print(sol.firstMissingPositive(arr))