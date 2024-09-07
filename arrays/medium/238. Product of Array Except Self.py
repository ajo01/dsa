class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        right = [1] * len(nums)
        res = [1] * len(nums)

        pre=1
        for i in range(len(nums)):
            left[i] = pre
            pre *= nums[i]

        post=1
        for i in range(len(nums)-1, -1, -1):
            right[i] = post
            post *= nums[i]

        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        
        return res
    

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        product = [1] * length
        for i in range(1, length):
            product[i] = product[i-1] * nums[i-1]
        
        right = [1] * length
        for i in range(length - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
            product[i] *= right[i]

        return product
    


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# brute force

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        copy = [1] * len(nums)
        for i in range(len(nums)):
            prod = 1 #
            j = 0
            for j in range(len(nums)):
                if j != i:
                    prod *= nums[j]
                j+=1
            copy[i] = prod
        return copy
            

# only for nums with non zero elements
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        copy = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]

        for i in range(len(nums)):
            copy[i] = prod / nums[i]
        return copy