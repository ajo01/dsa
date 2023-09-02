class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set()
        s1 = set(nums1)

        for i in range(len(nums2)):
            if nums2[i] in s1:
                s.add(nums2[i])
        return s