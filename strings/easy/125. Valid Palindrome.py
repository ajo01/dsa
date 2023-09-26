class Solution:
    def isPalindrome(self, s: str) -> bool:
        alph_list = list(filter(str.isalnum, s.lower()))
        l = 0
        r = len(alph_list) - 1

        while l <= r:
            if alph_list[l] != alph_list[r]:
                return False
            l+=1
            r-=1
        return True
