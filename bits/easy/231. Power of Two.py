
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if n == 1:
            return True
        while n % 2 == 0:
            n = n // 2
        return n == 1
        

#  4 is 100      100 AND 11 is 000
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        