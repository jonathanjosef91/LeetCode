class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zeros = 0
        zeroIndex = 0
        multi = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros += 1
                zeroIndex = i
            else:
                multi *= nums[i]
            if zeros >= 2:
                return [0]*len(nums)

        if zeros == 1:
            out = [0]*len(nums)
            out[zeroIndex] = multi
            return out

        out = [1]*len(nums)
        for i in range(1, len(out)):
            out[i] = nums[i-1]*out[i-1]

        last = 1
        for i in range(len(nums)-2, -1, -1):
            last = last * nums[i+1]
            out[i] *= last

        return out

sol = Solution()
arr = [6, 0, 7, 0]
print(sol.productExceptSelf(arr))