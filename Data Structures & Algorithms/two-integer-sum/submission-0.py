class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for idx, n in enumerate(nums):
            if n in complement:
                return [complement[n], idx]
            complement[target-n] = idx