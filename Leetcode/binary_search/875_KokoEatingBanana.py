# Solution 1
import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p/k)
            return hours <= h
        
        l = 1
        r = max(piles)

        while l < r:
            k = (l+r)//2

            if k_works(k):
                r = k
            else:
                l = k+1
        return l
    


# Solution 2
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)

        res = r

        while l <= r:
            k = (l+r)//2
            hours = 0

            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                res = min(res,k)
                r = k-1
            else:
                l = k+1
        return res