class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        elif n % 3 == 0:
            cnt = n // 3
            return 3 ** cnt
        elif n % 3 == 1:
            cnt = n // 3
            return (3 ** (cnt - 1)) * 4
        else:
            cnt = n // 3
            return 3 ** cnt * 2
            
        