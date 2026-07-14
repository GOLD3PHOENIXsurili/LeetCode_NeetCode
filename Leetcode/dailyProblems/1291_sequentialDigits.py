class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1,10))

        while queue:
            n = queue.popleft()
            if n > high:
                continue
            if low <= n <= high:
                res.append(n)
            ones = n%10
            if ones < 9:
                queue.append(n*10 + (ones +1))
        return res




# Generating sequential number approach

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1,10):
            num = i

            for j in range(i+1,10):
                num = num*10 + j

                if low <= num <= high:
                    ans.append(num)
        
        ans.sort()
        return ans
    


#Sliding window approach

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = "123456789"
        ans = []

        for length in range(2,10):
            for start in range(10-length):
                num = int(digits[start:start+length])

                if low <= num <= high:
                    ans.append(num)
        
        return ans