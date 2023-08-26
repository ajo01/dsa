class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        res = 1
        max = 1

        s = set(nums)
        arr = list(s)
        arr.sort()

        for i in range(1, len(arr)):
            if arr[i-1] + 1 == arr[i]:
                res +=1
                if res > max:
                    max = res
            else:
                res = 1
        return max