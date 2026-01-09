from bisect import bisect_right
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        total=m+n
        mid=total//2
        prev, curr, i, j =0,0,0,0

        for _ in range(mid+1):
            prev=curr
            if i<m and (j>=n or nums1[i]<=nums2[j]):
                curr=nums1[i]
                i+=1
            else:
                curr=nums2[j]
                j+=1
        
        if total%2==1:
            return curr
        return (curr+prev)/2




        