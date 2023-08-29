


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            x = right - left
            y = min(height[left], height[right])
            area = x * y
            maxArea = max(area, maxArea)

            if height[left] < height[right]:
                left +=1
            else:
                right -=1
        return maxArea

# brute force
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         maxA = 0
#         x = 0
#         y = 0
#         for i in range(0, len(height) - 1):
#             for j in range(i+1, len(height)):
#                 y = min(height[i], height[j])

#                 x = j - i
#                 area = y * x
#                 maxA = max(area, maxA)

#         return maxA