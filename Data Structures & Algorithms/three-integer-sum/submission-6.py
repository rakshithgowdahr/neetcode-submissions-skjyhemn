class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        for i, n1 in enumerate(nums):
            target = -(n1)
            hash_map = dict()
            for j, n2 in enumerate(nums[i+1:]):
                if target-n2 in hash_map:
                    triplets.append([nums[i], nums[j+i+1], nums[hash_map[target-n2]]])
                else:
                    hash_map[n2] = j+i+1
        output = []
        for triplet in triplets:
            if tuple(sorted(triplet)) not in hash_map:
                output.append(triplet)
                hash_map[tuple(sorted(triplet))] = True
        return output
