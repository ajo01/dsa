# not optimal

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        
        for i in range(len(s)):
            seen = set() 
            length = 1  
            seen.add(s[i])  
            for j in range(i + 1, len(s)):
                if s[j] in seen:
                    break   
                else:
                    length += 1
                    seen.add(s[j])
            max_length = max(max_length, length)

        return max_length
