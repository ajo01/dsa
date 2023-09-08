class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        res = [[1]]
        for i in range(1, numRows):
            prev = res[-1]
            cur = [1]
            for j in range(1, len(prev)):
                cur.append(prev[j-1]+prev[j])
            cur.append(1)
            res.append(cur)
        return res
