class Solution(object):
    def longestPalindrome(self, s):
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right +=1
            return s[left + 1: right]

        longest = ""
        for i in range(0, len(s)):
            #odd
            p1 = expand(i, i)
            #even
            p2 = expand(i, i+1)

            if len(p1) > len(longest):
                longest = p1
                
            if len(p2) > len(longest):
                longest = p2
        return longest
        
            
