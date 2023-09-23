
# two pointers
# O(n+m)
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
# O(n+m)log(n+m)

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