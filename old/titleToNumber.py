class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        col = 0
        for i in s:
            col *= int(ord('Z')-ord('A') + 1)
            col += int(ord(i)-ord('A')+1)

        return col

sol = Solution()
print(sol.titleToNumber(""))