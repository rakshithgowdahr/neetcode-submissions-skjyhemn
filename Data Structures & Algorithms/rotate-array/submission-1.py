class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # (i+k)% len
        # (1+4) %8
        # (2+4) %8
        hash_map = defaultdict(int)
        n = len(nums)
        for i, num in enumerate(nums):
            hash_map[i] = num
        for i in range(len(nums)):
            nums[i] = hash_map[(i-k)%n]