# brute
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = 0
        used = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i], nums[j]) not in used and nums[j] - nums[i] == k:
                    used.add((nums[i], nums[j]))
                    count+=1
        return count
        
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        d = {}
        for n in nums:
            if n in d:
                d[n] = d[n] + 1
            else:
                d[n] = 1
        if k > 0:
            # count the number of pairs (n, n+k) where both n and n+k are keys in the dictionary d
            ans = sum(n + k in d for n in d.keys())
        else:
            ans = sum(count > 1 for count in d.values())

        return ans