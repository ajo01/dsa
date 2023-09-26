
#optimal
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        l = 0
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum+=nums[r]

            while cur_sum >= target:
                min_length=min(min_length, r - l + 1)
                cur_sum-=nums[l]
                l+=1
        return min_length if min_length != float('inf') else 0

# first attempt. slow

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = sys.maxsize
        for l in range(len(nums)):
            r = len(nums) - 1

            while l <=r :
                if target <= sum(nums[l:r+1]):
                    min_length = min(min_length, r - l + 1)
                else:
                    r-=1

        return min_length if min_length != min_length else 0
    
