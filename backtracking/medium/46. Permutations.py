

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(arr, path):
            if not arr:
                res.append(path)
            for i in range(len(arr)):
                backtrack(arr[:i]+arr[i+1:], path+[arr[i]])
        backtrack(nums, [])
        return res
    

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

#                                               [1, 2, 3]
#                   backtrack([2, 3], [1])                              backtrack([1, 3], [2])                          backtrack([1, 2], [3])
#  backtrack([3], [1, 2])   backtrack([2], [1, 3])      backtrack([3], [2, 1])  backtrack([1], [2, 3])     backtrack([2], [3, 1])   backtrack([1], [3, 2]) 
#  backtrack([], [1, 2, 3]) backtrack([], [1, 3, 2])    backtrack([], [2, 1, 3]) backtrack([], [2, 3, 1])   backtrack([], [3, 1, 2]) backtrack([], [3, 2, 1])
#   res = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

