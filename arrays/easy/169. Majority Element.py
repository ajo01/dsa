class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        majority = len(nums)/2
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        for num in dict:
            if dict[num] >= majority:
                return num
        return -1
        

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         return nums[int(len(nums)/2)]
        
    