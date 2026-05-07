class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c = Counter(nums)
        del c[val] #{2:1, 3:1, 4:1}
        i = 0
        for key in c.keys():
            cnt = c[key]
            for _ in range(cnt):
                nums[i] = key
                i += 1
        return i