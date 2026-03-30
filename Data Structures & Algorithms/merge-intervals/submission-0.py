class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals = sorted(intervals, key=lambda x:x[0])
        curr_start_i, curr_end_i = intervals[0]
        i = 0
        merged_intervals = []
        while i < len(intervals)-1:
            next_start_i, next_end_i = intervals[i+1]
            if next_start_i >= curr_start_i and next_start_i <= curr_end_i:
                curr_end_i = max(curr_end_i, next_end_i)
            else:
                merged_intervals.append([curr_start_i, curr_end_i])
                curr_start_i, curr_end_i = next_start_i, next_end_i
            i += 1
        merged_intervals.append([curr_start_i, curr_end_i])
        return merged_intervals