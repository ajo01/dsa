class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left, cur_sum, max_len = 0, 0, 0

        target = sum(nums) - x
        n = len(nums)

        if target == 0:
            return n

        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and target < cur_sum:
                cur_sum -= nums[left]
                left += 1
            if target == cur_sum:
                max_len = max(max_len, right - left + 1)


        return n - max_len if max_len else -1