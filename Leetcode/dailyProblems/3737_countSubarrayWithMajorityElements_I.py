# brute Force O(N^2)

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            targetCount = 0
            for j in range(i,n):
                if nums[j] == target:
                    targetCount += 1
                
                sublen = j-i +1
                if targetCount > sublen//2:
                    ans += 1
            
        return ans
    
    