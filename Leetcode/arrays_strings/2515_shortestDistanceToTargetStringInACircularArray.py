class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        result = float('inf')

        for i in range(n):
            if words[i] == target:
                straightDistance = abs(i - startIndex)
                circularDistnce = n - straightDistance

                result = min(result,straightDistance,circularDistnce)
        
        return -1 if result == float('inf') else result