class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-2):
            target = -sorted_nums[i]
            l, r = i+1, len(sorted_nums)-1
            while l < r:
                s = sorted_nums[l] + sorted_nums[r]
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    triplets.add(tuple([sorted_nums[i], sorted_nums[l], sorted_nums[r]]))
                    l += 1
                    r -= 1
        return list(triplets)
