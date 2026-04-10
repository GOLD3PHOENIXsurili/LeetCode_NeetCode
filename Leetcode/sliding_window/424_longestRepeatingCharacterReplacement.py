class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0

        counts = [0]*26
        for r in range(len(s)):
            counts[ord(s[r]) - 65] += 1
            while (r-l+1) - max(counts) > k:
                counts[ord(s[l]) - 65 ] -= 1
                l += 1
            
            longest =max(longest, r-l+1)
        
        return longest
    



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        # maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)

            while (r-l+1) - max(count.values()) >k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res
    


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxf = max(maxf, count[s[r]])

            while (r-l+1) - maxf >k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        
        return res