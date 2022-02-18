class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        r = len(mat)
        c = len(mat[0])

        temp = [[0] * c for i in range(r)]
        answer = [[0] * c for i in range(r)]

        # initialise the first column
        for i in range(r):
            res = 0
            for delta_c in range(K + 1):
                if delta_c < c:
                    res += mat[i][delta_c]
            temp[i][0] = res

        # initialise slide the array by adding the new and removing the tail
        for i in range(r):
            res = temp[i][0]
            for j in range(1, c):
                # remove -k column + K column
                remove_c = j - K - 1

                if (0 <= remove_c < c):
                    res -= mat[i][remove_c]

                add_c = j + K
                if (0 <= add_c < c):
                    res += mat[i][add_c]

                temp[i][j] = res

            # initialise the first row by the same concept. but copy from the accumulated column value
        for i in range(c):
            res = 0
            for delta_r in range(K + 1):
                res += temp[delta_r][i]
            answer[0][i] = res

        for i in range(c):
            res = answer[0][i]
            for j in range(1, r):
                # remove -k row + K row
                remove_r = j - K - 1

                if (0 <= remove_r < r):
                    res -= temp[remove_r][i]

                add_r = j + K
                if (0 <= add_r < r):
                    res += temp[add_r][i]

                answer[j][i] = res

        return answer

mat = [[1,2,3],[4,5,6],[7,8,9]]
sol = Solution()
print(sol.matrixBlockSum(mat,1))
