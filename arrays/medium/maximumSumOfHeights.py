
# leetcode contest 364

# accepted solution
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        d = {}
        res = 0
        
        
        for i in range(len(maxHeights)):
            d[i] = maxHeights[i]
        
        for pIndex in d:
            copied = maxHeights.copy()
            
            for i in range(pIndex, 0, -1):
                if copied[i - 1] > copied[i]:
                    copied[i - 1] = copied[i]
            for i in range(pIndex+1, len(maxHeights)-1):
                if copied[i + 1] > copied[i]:
                    copied[i + 1] = copied[i]
            

            possibleSum = sum(copied)
            res = max(res, possibleSum)
        return res


# looping through peaks only
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        d = {}
        res = 0
        maxVal = 0
        
        
        for i in range(len(maxHeights)):
            if maxHeights[i] >= maxVal:
                d[i] = maxHeights[i]
                maxVal = maxHeights[i]
        
 
        d = {key: value for key, value in d.items() if value == maxVal}
        print(d, maxVal)
        
        for pIndex in d:
            copied = maxHeights.copy()
            
            for i in range(pIndex, 0, -1):
                if copied[i - 1] > copied[i]:
                    copied[i - 1] = copied[i]
            for i in range(pIndex+1, len(maxHeights)-1):
                if copied[i + 1] > copied[i]:
                    copied[i + 1] = copied[i]
            
            print(copied)
            possibleSum = sum(copied)
            res = max(res, possibleSum)
        return res



# naive solution : considering only one possible peak
class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        peak = 0
        pIndex = 0
        sum = 0
        
        for i in range(len(maxHeights)):
            if maxHeights[i] > peak:
                peak = maxHeights[i]
                pIndex = i
        for i in range(pIndex, 0, -1):
            if maxHeights[i - 1] > maxHeights[i]:
                maxHeights[i - 1] = maxHeights[i]
        for i in range(pIndex+1, len(maxHeights)-1):
            if maxHeights[i + 1] > maxHeights[i]:
                maxHeights[i + 1] = maxHeights[i]
            
        for h in maxHeights:
            sum += h
        return sum


# [5,3,4,1,1]  # [5,3,3,1,1]   13
# [6,5,3,9,2,7]  # [3,3,3,9,2,2]  22
# [3,2,5,5,2,3]   # [2,2,5,5,2,2]  13
# [5,2,4,4]  ? [4, 4, 4, 4]   # 12