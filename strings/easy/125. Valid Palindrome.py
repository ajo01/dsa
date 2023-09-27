# O(1) space O(n) time
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            if l > r or s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True

# O(n) space O(n) time
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
