class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = [[] for _ in range(2)] 

        s1 = set(nums1)
        s2 = set(nums2)

        ans1 = []
        ans2 = []
        for n in s1:
            if n not in s2:
                ans1.append(n)
        for n in s2:
            if n not in s1:
                ans2.append(n)
        ans[0] = ans1
        ans[1] = ans2
        return ans

        