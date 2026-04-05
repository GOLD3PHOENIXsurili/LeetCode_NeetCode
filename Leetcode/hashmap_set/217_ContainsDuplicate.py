class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # n = len(nums)
        # # for i in range(n):
        # #     for j in range(i+1,n):
        # #         if nums[i] == nums[j]:
        # #             return True
        # # return False

        # A = set(nums)
        # return len(nums) != len(A)


        h = set()

        for num in nums:
            if num in h:
                return True
            else:
                h.add(num)
        return False