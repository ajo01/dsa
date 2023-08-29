class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k ==0: return False
        _set = set()

        for i in range(0, len(nums)):
            if nums[i] in _set: return True
            _set.add(nums[i])
            if len(_set) == k+1:
                _set.remove(nums[i-k])
        return False