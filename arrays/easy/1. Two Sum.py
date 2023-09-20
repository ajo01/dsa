class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List[int] 
        d = {}
        for i in range(0, len(nums) ):
            n = target-nums[i]
            if n in d:
                return [i, d[n]]
            d[nums[i]] = i

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List[int] 
        map = {}

        for i in range(0, len(nums)):
            map[nums[i]] = i

        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in map and map[complement] !=i:
                return [i, map[complement]]
            
        return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        List[int] 
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []