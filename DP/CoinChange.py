import unittest
from heapq import heapify, heappush, heappop

class Solution(object):
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
                oldVal = change.get(i+c, -1)
                if oldVal == -1:
                    heappush(heap, i + c)
                    change[i + c] = change[i] + 1
                else:
                    change[i + c] = min(oldVal, change[i] + 1)

        return change.get(amount, -1)

    def coinChange_v1(self, coins, amount):
        """
        O(amount * coins) -> Got TO
        """
        change = {0: 0}

        for i in range(amount):
            if i not in change.keys():
                continue

            for c in coins:
                change[i + c] = min(change.get(i + c, amount), change[i] + 1)

        return change.get(amount, -1)


class test_CoinChange(unittest.TestCase):
    def test_1(self):
        self.assertEqual(3, Solution().coinChange(coins = [1,2,5], amount = 11))
        self.assertEqual(-1, Solution().coinChange(coins = [2], amount = 3))
        self.assertEqual(0, Solution().coinChange(coins = [1], amount = 0))
