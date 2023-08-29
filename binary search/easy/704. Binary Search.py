class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo)//2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid
        if target != nums[lo]:
            return -1
        return lo
