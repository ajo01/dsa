# O(n+m)log(n+m)  space O(1)
# binary search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        lo = 0
        hi = n1
        n = n1 + n2
        left = (n + 1) // 2


        while lo <= hi:
            mid1 = (lo + hi)//2
            mid2 = left - mid1

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('-inf')
            r2 = float('-inf')

            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 -1]

            if l1 <= r2 and l2 <= r1: 
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2))/2.0
            elif l1 > r2: 
                hi = mid1 - 1
            else: 
                lo = mid1 + 1
        return 0
        

# two pointers
# time O(n+m)  space O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0 # median 
        m2 = 0 # prev

        halfPos = (n+m)//2

        for _ in range(halfPos + 1):
            m2 = m1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j+=1
                else:
                    m1 = nums1[i]
                    i+=1
            elif i < n:
                m1 = nums1[i]
                i+=1
            else:
                m1 = nums2[j]
                j+=1
        if (n+m)%2 == 1:
            return float(m1)
        else:
            return (float(m1) + float(m2))/2.0
        


# brute force
# time O(n+m) space O(n+m)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0
        arr = nums1+nums2
        arr.sort()

        n = len(arr)

        if n % 2 == 1:
            median = arr[n//2]
        else:
            median =( arr[n//2 -1] + arr[n//2] )/2
        return median