# [2, 0, 1] -> [1, 0, 2] -> [1, 0, 2] -> [0, 1, 2]
#   0 0 2        0 0 1         0 1 1       1 2 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        red = 0
        white = 0
        blue = len(nums) - 1

        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red +=1
                white +=1
            elif nums[white] == 1:
                white+=1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -=1