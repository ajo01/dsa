class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        first = nums[-1]
        second = nums[-2]
        third = nums[-3]

        negFirst = nums[0]
        negSecond = nums[1]
        return max(first * second * third, first * negFirst * negSecond)
        