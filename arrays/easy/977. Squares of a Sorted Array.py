class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(0, len(nums)):
            val = nums[i]**2
            arr.append(val)
        arr.sort()
        return arr