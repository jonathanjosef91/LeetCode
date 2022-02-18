def getNewRowSum(mat, r, k):
    m = len(mat)
    n = len(mat[0])
    sum = 0
    for i in range(0,min(n,k+1)):
        for j in range(max(0,r-k),min(m,r+(k+1))):
            sum += mat[j][i]
    return sum

def getColSum(mat,r,c,k):
    m = len(mat)
    sum = 0
    for i in range(max(0,r-k),min(m,r+k+1)):
        sum += mat[i][c]
    return sum

class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        ans = [[0 for i in range (n)] for j in range(m)]
        sum = 0

        for r in range(m):
            sum = getNewRowSum(mat, r, k)
            ans[r][0] = sum
            for c in range(1,n):
                if c+k<n:
                    sum += getColSum(mat,r,c+k,k)
                if c-k-1>=0:
                    sum -= getColSum(mat,r,c-k-1,k)
                ans[r][c]=sum

        return ans

#mat = [[1,2,3],[4,5,6],[7,8,9]]
#print(getColSum(mat,1,1,1))
#sol = Solution()
#print(sol.matrixBlockSum(mat,1))
#print(getNewRowSum(mat,3,2))

mat2 = [[0]*3]*3
mat2[0][0] = 1
mat2 == 1

def calcBox(mat,r,c,k):
    m = len(mat)
    n = len(mat[0])
    sum = 0
    for i in range(max(0,c-k),min(n,c+(k+1))):
        for j in range(max(0,r-k),min(m,r+(k+1))):
            sum += mat[j][i]
    return sum

class SolutionBad(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        ans = [[0 for i in range (n)] for j in range(m)]
        sum = 0

        for r in range(m):
            for c in range(n):
                ans[r][c] = calcBox(mat,r,c,k)

        return ans
#max(0,c-k),min(m,c+k))
#print(ans)