import unittest
from Tags import *
"""
Author: Jonathan Joseph
Problem Description/link: https://leetcode.com/problems/top-k-frequent-words/
"""

class Solution(object):
    def getTags(self):
        tags = [Difficulty.Medium, Topic.Strings]
        return tags

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        occ = {}
        for word in words:
            occ[word] = occ.get(word, 0) - 1

        l = []
        for w, v in occ.items():
            l.append((v, w))

        l.sort()

        return [word[1] for word in l][:k]



class test_topKFrequent(unittest.TestCase):
    def test_1(self):
        self.assertEqual(["i","love"], Solution().topKFrequent(words=["i", "love", "leetcode", "i", "love", "coding"], k=2))
        self.assertEqual(["the","is","sunny","day"], Solution().topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
