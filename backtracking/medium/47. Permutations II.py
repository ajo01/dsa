class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        def backtrack(arr, path):
            if len(arr) == 0:
               if path not in res:
                   res.append(path)
               return
            for i in range(len(arr)):
                backtrack(arr[:i]+arr[i+1:], path + [arr[i]])
            
        
        backtrack(nums, [])
        return res