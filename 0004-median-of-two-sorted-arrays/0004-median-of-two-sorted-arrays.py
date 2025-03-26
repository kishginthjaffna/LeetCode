class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged = []
        i, j = 0, 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        length = len(merged)
        if length % 2 == 1:
            return merged[length // 2]
        else:
            mid1, mid2 = length // 2 - 1, length // 2
            return (merged[mid1] + merged[mid2]) / 2.0
