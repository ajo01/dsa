class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for n in nums:
            tmp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = tmp

        return rob2
    


class Solution:

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        memo = [0 for _ in range(n+1)]
        memo[0] = 0
        memo[1] = nums[0]
        for i in range(1, n):
            memo[i+1] = max(memo[i], memo[i-1] + nums[i])
        return memo[n]




class Solution:
    def __init__(self):
        self.memo = []

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return max(nums)
        self.memo = [-1 for _ in range(n)]
        return self.robH(nums, n - 1)

    def robH(self, nums: List[int], i: int) -> int:
        if i < 0:
            return 0
        if self.memo[i] >= 0:
            return self.memo[i]
        res = max(self.robH(nums, i-1), self.robH(nums, i-2) + nums[i])
        self.memo[i] = res
        return res



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums)
        return self.robH(nums, len(nums) - 1)

    def robH(self, nums: List[int], i: int) -> int:
        if i < 0:
            return 0
        return max(self.robH(nums, i-1), self.robH(nums, i-2) + nums[i])