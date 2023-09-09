# dp[0] = 1
# dp[1] = 1
# dp[2] = 2   dp[0] + dp[1]
# dp[3] = 4   
# dp[4] = 7
# dp[5] = 13

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]

        return dp[target]