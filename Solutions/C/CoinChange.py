import unittest
from Tags import *

from heapq import heapify, heappush, heappop

"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""

class Solution(object):
    def getTags(self):
        tags = [Difficulty.Medium, Topic.DP]
        return tags

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        change = {0: 0}
        heap = [0]
        heapify(heap)

        while len(heap) > 0:
            i = heappop(heap)
            if i >= amount:
                break

            for c in coins:
                oldVal = change.get(i + c, -1)
                if oldVal == -1:
                    heappush(heap, i + c)
                    change[i + c] = change[i] + 1
                else:
                    change[i + c] = min(oldVal, change[i] + 1)

        return change.get(amount, -1)


class test_coinChange(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, Solution().coinChange(coins=[1,2,5], amount=11))
        self.assertEqual(-1, Solution().coinChange(coins=[2], amount=3))
        self.assertEqual(0, Solution().coinChange(coins=[1], amount=0))
