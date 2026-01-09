from bisect import bisect_right
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        final=list(nums1)
        for n in nums2:
            i=bisect_right(final,n)
            final.insert(i,n)
        m=len(nums1)
        n=len(nums2)
        mid=(n+m)//2
        if (n+m)%2==0:
            return (final[mid-1]+final[mid])/2
        else:
            return final[mid]


        