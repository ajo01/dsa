# multiple of 5 then 1 trailing zero

# 5! = 120    cnt: 1
# 6! = 720    cnt: 1
# 10! = 3628800   cnt: 2

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt =0
        while n != 0:
            n = n//5
            cnt += n
        return cnt