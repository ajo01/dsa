class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
       
        intervals.append(newInterval)
        intervals = sorted(intervals)
        res = [intervals[0]]
        for start, end in intervals:
            last = res[-1][1]

            if last >= start:
                res[-1][1] = max(last, end)
            else:
                res.append([start, end])

        return res