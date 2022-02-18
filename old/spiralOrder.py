class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []


        m = len(matrix)
        n = len(matrix[0])

        sr = sc = 0
        er = m
        ec = n
        out = []

        while sr < er and sc < ec:
            out += self.__takeFrame(matrix,sr,er,sc,ec)
            sr += 1
            sc += 1
            er -= 1
            ec -= 1

        return out

    def __takeFrame(self, matrix, sr, er, sc, ec):
        frame = []

        if sr+1 >= er:
            frame[:] = matrix[sr][sc:ec]
            return frame

        if sc+1 >= ec:
            for r in range(sr,er):
                frame += [matrix[r][sc]]
            return frame

        for c in range(sc,ec):
            frame += [matrix[sr][c]]
        for r in range(sr+1,er):
            frame += [matrix[r][ec-1]]
        for c in range(ec-2,sc-1,-1):
            frame += [matrix[er-1][c]]
        for r in range(er-2,sr,-1):
            frame += [matrix[r][sc]]

        return frame


"""
mat =[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
sol = Solution()
print(sol.spiralOrder(mat))"""