class Solution(object):
    def groupAnagrams(strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        indexes = {}
        rList = []
        ri = 0
        for i in strs:
            templ = list(i)
            templ.sort()
            temp = str(templ)
            if temp not in indexes:
                indexes[temp] = ri;
                ri += 1
                rList += [[]]
            rList[indexes[temp]] += [i]
        return rList

print(Solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))