class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()   
        total_length = len(merged)

        if total_length % 2 == 0:
            return (merged[(total_length//2)-1] + merged[total_length//2]) / 2
        else:
            return merged[total_length//2]