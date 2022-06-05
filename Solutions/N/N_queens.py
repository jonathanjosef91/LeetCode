import unittest
from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: https://leetcode.com/problems/n-queens-ii/
"""

class Solution(object):
    def getTags(self):
        tags = [Difficulty.Hard, Topic.Algorithms]
        return tags

    def _checkMoveForDiag(self, RowPerCol, nextCol, nextRow, n):
        for c in range(nextCol):
            r = RowPerCol[c]
            d_x = nextCol - c
            if r == nextRow + d_x or r == nextRow - d_x:
                return False

        return True

    def _placeNextQueen(self, RowPerCol, nextCol, n):
        if nextCol == n:
            return 1

        count = 0
        for r in range(n):
            if r not in RowPerCol and self._checkMoveForDiag(RowPerCol, nextCol=nextCol, nextRow=r, n=n):
                rowPerCol = RowPerCol + [r]
                count += self._placeNextQueen(rowPerCol, nextCol=nextCol+1,n=n)

        return count


    def totalNQueens(self, n):
        return self._placeNextQueen([], 0, n)


class test_n_queens(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, Solution().totalNQueens(2))
        self.assertEqual(0, Solution().totalNQueens(3))
        self.assertEqual(2, Solution().totalNQueens(4))
