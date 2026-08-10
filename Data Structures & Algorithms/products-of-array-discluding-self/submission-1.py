class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = list(nums)
        suffix = list(nums)
        output = []
        for idx in range(1, len(nums)):
            prefix[idx] = prefix[idx-1] * prefix[idx]
        print("prefix", prefix)
        for idx in range(len(nums)-2, 0, -1):
            suffix[idx] = suffix[idx+1] * suffix[idx]
        print("suffix", suffix)
        for idx in range(len(nums)):
            if idx == 0:
                output.append(suffix[idx+1])
            elif idx == len(nums)-1:
                output.append(prefix[idx-1])
            else:
                output.append(prefix[idx-1]*suffix[idx+1])
        return output