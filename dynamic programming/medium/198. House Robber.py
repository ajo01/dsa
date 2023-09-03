# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         rob1, rob2 = 0,0
#         for n in nums:
#             tmp = max(rob1 + n, rob2)
#             rob1 = rob2
#             rob2 = tmp

#         return rob2
    


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
