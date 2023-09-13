class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -sys.maxsize  # this line is important
        sum = 0

        for num in nums:
            sum += num
            if sum > maxSum:
                maxSum = sum
            if sum < 0:
                sum = 0
        return maxSum
            
        