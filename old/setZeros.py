"""Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        if not matrix or not matrix[0]:
            return

        indexRow = -1
        indexCol = -1

        #find row without a zero
        for r in range(len(matrix)):
            if matrix[r].count(0) == 0:
                indexRow = r
                break

        #find col without a zero
        for c in range(len(matrix[0])):
            count = 0
            for r in range(len(matrix)):
                if matrix[r][c] == 0:
                    count += 1
                    break
            if count == 0:
                indexCol = c
                break

        if indexRow == -1 or indexCol == -1:
            for r in range(len(matrix)):
                for c in range(len(matrix[0])):
                    matrix[r][c] = 0
            return


        for r in range(len(matrix)):
            if r == indexRow:
                continue
            for c in range(len(matrix[0])):
                if c == indexCol:
                    continue
                if matrix[r][c] == 0:
                    matrix[r][indexCol] = 0
                    matrix[indexRow][c] = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[indexRow][c] == 0 or matrix[r][indexCol] == 0:
                    matrix[r][c] = 0


sol = Solution()
"""
mat = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
"""
mat = [[0,1]]
sol.setZeroes(mat)
print(mat)