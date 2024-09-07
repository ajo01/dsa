
# input nums = [1,2,3]
# res: []
#   [[], [1], [2], [3]]

#  start                  1       2                      
#  [[], [1], [2], [3], [1, 2], [2, 3], [3]]

# optimal

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, start):
            res.append(arr.copy())   # arr[:] also works
            for i in range(start, len(nums)):
                arr.append(nums[i])
                backtrack(arr, i+1)
                arr.pop()
        backtrack([],0)
        return res

# very slow, not optimal
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr):
            if arr not in res:
                res.append(arr)
            for i in range(len(arr)):
                backtrack(arr[:i]+arr[i+1:])
        backtrack(nums)
        return res