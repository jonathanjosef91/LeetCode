from functools import cmp_to_key

class Solution(object):
    def _cmpNum(self, x, y):
        if str(x) + str(y) > str(y) + str(x):
            return 1
        else:
            return -1

    def largestNumber(self, nums):
        nums.sort(key=cmp_to_key(self._cmpNum), reverse=True)
        s = ""
        for i in nums:
            s += str(i)

        while len(s) > 1 and s[0] == "0":
            s = s[1:]

        return s

if __name__ == '__main__':
    print(Solution().largestNumber([12341,123411234]))
    print(Solution().largestNumber([432,43243]))
    print(Solution().largestNumber([0,0]))

    print(Solution().largestNumber([3,30,34,5,9]))
    print(Solution().largestNumber([10, 2]))
    print(Solution().largestNumber([2, 10]))
