# class Solution:
#     def sortedSquares(self,nums:List[int]) -> List[int]:
#         n = len(nums)
#         left = 0
#         right = n-1
#         ans = []

#         while left <= right:
#             if abs(nums[left]) > abs(nums[right]):
#                 ans.append(nums[left]**2)
#                 left += 1
#             else:
#                 ans.append(nums[right]**2)
#                 right -= 1

        
#         ans.reverse()
#         return ans

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n -1
        pos = n-1
        ans = [0]*n

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                ans[pos] = nums[left]**2
                left += 1
            else:
                ans[pos] = nums[right]**2
                right -= 1
            pos -= 1
        return ans
        
