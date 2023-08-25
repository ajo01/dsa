class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]: 
        length = len(nums)
        ans = []
        nums.sort()
        for i in range(1, length):
            if nums[i-1] == nums[i]:
                ans.append(nums[i-1])
        return ans