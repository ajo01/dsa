class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            if len(path) == k:
                res.append(path)
                return
            
            for i in range(index, n+1):
                backtrack(i+1, path+[i])

        backtrack(1, [])
        return res
        
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

#     backtrack(2, [1])                                                                        backtrack(3, [2])                                        backtrack(4, [3])
#     backtrack(3, [1, 2])    backtrack(4, [1, 3])     backtrack(5, [1, 4])                    backtrack(4, [2, 3]) backtrack(5, [2, 4])                backtrack(5, [3, 4])  