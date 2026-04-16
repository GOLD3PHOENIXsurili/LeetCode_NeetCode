class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        min_length = float('inf')
        l = 0

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                min_length = min(min_length, r-l+1)
                summ -= nums[l]
                l += 1
        
        return min_length if min_length < float('inf') else 0

