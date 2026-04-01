from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for i in ransomNote:

            if i not in counter:
                return False
            elif counter[i] == 1:
                del counter[i]
            else:
                counter[i] -= 1
        
        return True


# counter = {}
# for c in magazine:
#     if c in counter:
#         counter[c] += 1
#     else:
#         counter[c] = 1



# counter = defaultdict(int)

# for c in magazine:
#     couner[c] += 1