class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        res = []
        i, n = 0, len(intervals)
        for i in range(n):
            start, end = intervals[i]
            if len(newInterval) and newInterval[0] <= start:
                intervals.append([newInterval.pop(0), newInterval.pop()])
            intervals.append([start, end])
        if len(newInterval):
            intervals.append(newInterval)
        intervals = intervals[n:]
        curr_start, curr_end = intervals[0]
        for start, end in intervals[1:]:
            if curr_end >= start:
                curr_end = max(curr_end, end)
            else:
                res.append([curr_start, curr_end])
                curr_start, curr_end = start, end
        res.append([curr_start, curr_end])
        return res