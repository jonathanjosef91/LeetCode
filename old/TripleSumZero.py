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
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            numsMap = createdict(nums[i+1:])
            for j in range(i + 1, len(nums) - 1):
                numsMap[nums[j]] -= 1
                reminder = (-1)*(nums[i]+nums[j])
                if reminder in numsMap and numsMap[reminder] > 0:
                    temp = [nums[i], nums[j], reminder]
                    temp.sort()
                    rList.append(list(temp))
        rList = removeDuplicate(rList)

        return rList

nums = [[1,1,3],[1,1,3],[2,3,4]]
nums = removeDuplicate(nums)
for i in range(5):
    print(i)
print(nums)