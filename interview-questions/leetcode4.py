class Solution:
    def mid(some_list):
        if len(some_list) % 2 == 1:
            mid = some_list // 2
            return (some_list[mid] + some_list[mid+1]) / 2
        
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        if(len(nums1) == 0):
            return mid(nums2)
        if(len(nums2) == 0):
            return mid(nums1)
        if(len(nums1) == 1 and len(nums2) == 1):
            return (nums1[0] + nums2[0]) / 2
        if(len(nums1) == 1 and len(nums2) == 2):
            if nums1[0] > nums2[0]:
                if nums1[0] < nums2[1]:
                    return nums1[0]
                return nums2[1]
            return nums2[0]
        if(len(nums1) == 2 and len(nums2) == 1):
            if nums2[0] > nums1[0]:
                if nums2[0] < nums1[1]:
                    return nums2[0]
                return nums1[1]
            return nums1[0]
        if(len(nums1) == 0 and len(nums2) == 2):
            return (nums2[0] + nums2[1]) / 2
        if(len(nums1) == 2 and len(nums2) == 0):
            return (nums1[0] + nums1[1]) / 2 
        mid1 = len(nums1) // 2
        mid2 = len(nums2) // 2
        if nums1[mid1] > nums2[mid2]:
            return self.findMedianSortedArrays(nums1[:mid1],nums2[mid2:])
        return self.findMedianSortedArrays(nums1[mid1:],nums2[:mid2])
       
print(Solution().findMedianSortedArrays([1,3],[2]))
print(Solution().findMedianSortedArrays([1,2],[3,4]))
