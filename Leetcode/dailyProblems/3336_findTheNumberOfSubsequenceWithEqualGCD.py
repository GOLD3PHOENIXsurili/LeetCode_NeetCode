from functools import cache
from math import gcd

MOD = 10**9 + 7
# Recursive DP + Memoization
class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        
        n = len(nums)
        @cache
        def dfs(i,s1,s2):
            if i == n:
                return 1 if s1== s2 and s1!=0 else 0
            
            x = nums[i]
            ans = dfs(i+1,s1,s2)
            ans += dfs(i+1,gcd(s1,x),s2)
            ans += dfs(i+1,s1,gcd(s2,x))

            return ans % MOD
        return dfs(0,0,0)



# Bottom Up DP
