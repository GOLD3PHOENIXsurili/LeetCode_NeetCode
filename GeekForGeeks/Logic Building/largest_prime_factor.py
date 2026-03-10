#User function Template for python3

class Solution:
    def largestPrimeFactor(self, n):
        # code here
        largesrPrime = -1
        
        while n%2 == 0:
            largestPrime = 2
            n = n//2
        
        i = 3
        while i*i <= n:
            while n% i == 0:
                largestPrime = i
                n //= i
            i += 2
        
        
        if n > 2:
            largestPrime = n
        
        return largestPrime
        
        