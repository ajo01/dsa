
# contest 364

# expect 001 -> 001   101 -> 101  011 -> 101  

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        countOnes = 0
        for letter in s:
            if letter == '1':
                countOnes += 1
 
        s = list(s)
        n = len(s)
        res = ['0'] *n 
        for i in range(n):
            if countOnes > 1:
                res[i] = '1' 
                countOnes -= 1
            else:
                res[i] = '0'
        if countOnes == 1:
            res[-1] = '1'
        res = ''.join(res)
        return res