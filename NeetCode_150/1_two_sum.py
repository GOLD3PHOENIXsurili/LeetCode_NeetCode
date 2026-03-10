class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1,n):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        n = len(nums)
        seen = {}

        for i in range(n):
            current = nums[i]
            need = target - current

            if need in seen:
                return [seen[need],i]
            
            seen[current] = i
            