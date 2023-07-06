import unittest
from typing import List

from Tags import *

"""
Author: Jonathan Joseph
Problem Description/link: replace with relevant link or problem description
"""


class Solution(object):
    def getTags(self):
        tags = [Difficulty.Beginners, Topic.Algorithms]
        return tags

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hist = {}
        for n in nums:
            hist[n] = hist.get(n, 0) + 1

        l = [(v, k) for k, v in hist.items()]
        return [k for v, k in sorted(l, reverse=True)][:k]


class test_topKFrequentNums(unittest.TestCase):
    def test_1(self):
        self.assertListEqual([1, 2], Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
