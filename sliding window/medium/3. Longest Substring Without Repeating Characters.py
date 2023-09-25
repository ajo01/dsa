# categories: arrays, strings, sliding window

#optimal 
# space O(n) n is input s
# time O(n)  going through all of s only once

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        n = len(s)
        l = 0
        charSet = set()
        for r in range(n):
            if s[r] not in charSet:
                charSet.add(s[r])
                max_length = max(max_length, r - l + 1)
            else:
                while s[r] in charSet:
                    charSet.remove(s[l])
                    l+=1
                charSet.add(s[r])
        return max_length




# not optimal
# brute force

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
