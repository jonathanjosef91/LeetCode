class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = []
        word = ""
        self.__genAux(out, 0, 0, n, word)
        return out

    def __genAux(self, out, index, numOfStarts, n, word):
        if numOfStarts > n:
            return

        if numOfStarts < index-numOfStarts:
            return

        if index == 2*n and numOfStarts == n:
            out += [word]
            return

        word += "("
        self.__genAux(out, index+1, numOfStarts+1, n, word)
        word = word[:len(word)-1]

        word += ")"
        self.__genAux(out, index+1, numOfStarts, n, word)
        word = word[:len(word)-1]



sol = Solution()
print(sol.generateParenthesis(14))