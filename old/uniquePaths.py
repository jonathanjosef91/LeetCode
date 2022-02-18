import math

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n <= 0:
            return 0

        if m  == 1 or n == 1:
            return 1

        numOfSteps = (m-1)+(n-1)
        return self.__nCr(numOfSteps, m-1)

    def __nCr(self, n, k):
        return self.__multiRange(k+1,n)/math.factorial(n-k)

    def __multiRange(self,start,end):
        if (start <= 0 or end <= 0 or start > end):
            return 1
        return start*(self.__multiRange(start+1, end))

sol = Solution()
m = 3
n = 7
print(sol.uniquePaths(m,n))