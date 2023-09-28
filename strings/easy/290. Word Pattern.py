# O(n) space time
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        s1 = s.split(' ')
        p = pattern       
        if len(s1) != len(p):
            return False
        if len(set(s1)) != len(set(p)):
            return False

    # map word to letter in p
        for i in range(len(s1)): 
            if s1[i] not in d:
                d[s1[i]] = p[i]
            elif d[s1[i]] != p[i]:
                return False

        return True

            
        