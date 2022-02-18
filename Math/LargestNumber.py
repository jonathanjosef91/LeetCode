import unittest
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


class test_largestNumber(unittest.TestCase):
    def test_1(self):
        self.assertEqual("12341123412341", Solution().largestNumber([12341,123411234]))
        self.assertEqual("43243432", Solution().largestNumber([432,43243]))
        self.assertEqual("0", Solution().largestNumber([0,0]))
        self.assertEqual("9534330", Solution().largestNumber([3,30,34,5,9]))
        self.assertEqual("210", Solution().largestNumber([10, 2]))
        self.assertEqual("210", Solution().largestNumber([2, 10]))