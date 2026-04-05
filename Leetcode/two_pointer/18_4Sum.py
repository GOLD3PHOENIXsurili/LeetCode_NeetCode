# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         n = len(nums)
#         answer = []
#         nums.sort() # chnage 

#         for i in range(n):   # chnage
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
            
#             for j in range(i+1,n):  # chnage
#                 if j > i+1 and nums[j] == nums[j-1]:
#                     continue
                
#                 lo, hi = j+1, n -1

#                 while lo < hi:
#                     summ = nums[i] + nums[j] + nums[lo] + nums[hi]

#                     if summ == target:
#                         answer.append([nums[i],nums[j],nums[lo],nums[hi]])
#                         lo += 1
#                         hi -= 1

#                         while lo < hi and nums[lo] == nums[lo-1]:
#                             lo += 1
#                         while lo < hi and nums[hi] == nums[hi-1]:  # chnage
#                             hi -= 1

#                     elif summ < target:
#                         lo += 1
#                     else:
#                         hi -= 1
#         return answer



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue

                lo, hi = j+1, n-1

                while lo < hi:
                    summ = nums[i] + nums[j] + nums[lo] + nums[hi]

                    if summ == target:
                        answer.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1

                        while lo < hi and nums[lo] == nums[lo-1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi+1]:
                            hi -= 1

                    elif summ < target:
                        lo += 1
                    else:
                        hi -= 1

        return answer