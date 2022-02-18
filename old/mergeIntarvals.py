class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) <= 0:
            return []

        intervals.sort()
        out = []
        start = end = intervals[0][0]

        for i in intervals:
            if i[0]<=end:
                end = max(end,i[1])
            else:
                out.append([start,end])
                start = i[0]
                end = i[1]

        out.append([start,end])

        return out




sol = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(sol.merge(intervals))