class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        def isPalindrome(str):
            reverse = str[::-1]
            return str == reverse

        if not s:
            return ""

        maxStr = ""

        for i in range(0, len(s)):
            for j in range(i+1, len(s)+1):
                str = s[i:j+1]
                if isPalindrome(str) and len(str) > len(maxStr): 
                    maxStr = str
        return maxStr
        
