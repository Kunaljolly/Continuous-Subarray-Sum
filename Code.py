class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sums[i+1] = prefix_sums[i] + nums[i]
        for start in range(len(nums)):
            for end in range(start + 2, len(nums) + 1):
                if (prefix_sums[end] - prefix_sums[start]) % k == 0:
                    return True
        return False
