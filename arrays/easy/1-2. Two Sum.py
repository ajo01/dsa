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