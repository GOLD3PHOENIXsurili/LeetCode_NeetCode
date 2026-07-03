class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            
            if ans == num:
                count += 1
            else:
                count -= 1
        
        return ans

        


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}

        for num in nums:
            freq[num] = freq.get(num,0)+1

        for num, count in freq.items():
            if count >len(nums)//2:
                return num