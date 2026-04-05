# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # O(nlogn)
#         # s = list(s)
#         # t = list(t)

#         # x = sorted(s)
#         # y = sorted(t)

#         # return x == y
        
#         # O(n)
#         if len(s) != len(t):
#             return False
#         count = {}
#         for char in s:
#             count[char] = count.get(char, 0) + 1
#         for char in t:
#             if char not in count or count[char] == 0:
#                 return False
#             count[char] -= 1
#         return True





from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dict = Counter(s)
        t_dict = Counter(t)

        return s_dict == t_dict