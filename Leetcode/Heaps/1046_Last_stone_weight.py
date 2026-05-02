import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)

            if largest != next_largest:
                heapq.heappush(stones, largest - next_largest)

        if len(stones) == 1:
            return -heapq.heappop(stones)
        else:
            return 0

# Time: O(n log n)
# Space: O(1)





import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, -(y-x))
        
        return -stones[0] if stones else 0

# Heap Build O(n)
# Each Operation O(logn)
# Total Complexity O(nlogn)
