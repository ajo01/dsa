class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_diff = sys.maxsize
        ans = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]

                diff = abs(target - sum)
                if target > sum:
                    j+=1
                elif target < sum:
                    k-=1
                else:
                    ans = sum
                    return ans
                        
                if diff < min_diff:
                    min_diff = diff
                    ans = sum
        return ans