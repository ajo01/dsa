class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = [intervals[0]]

        for start, end in intervals:
            lastElement = res[-1][1]

            if lastElement >= start:
                res[-1][1] = max(lastElement, end)
            else:
                res.append([start, end])

        return res