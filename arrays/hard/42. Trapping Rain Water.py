class Solution:
    def trap(self, height: List[int]) -> int:
 
        l, r = 0, len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res

class Solution:
    def trap(self, height: List[int]) -> int:
 
        maxLeft = [0] * (len(height) + 1)
        maxRight = [0] * (len(height) + 1)
        res = 0
        for i in range(0, len(height)):
            if i > 0:
                maxLeft[i] = max(height[:i])
            if i != len(height) - 1:
                maxRight[i] = max(height[i+1:])
            rain = min(maxLeft[i], maxRight[i]) - height[i]
            if rain > 0:
                res += rain

        return res