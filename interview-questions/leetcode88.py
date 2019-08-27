class Solution(object):
        
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        temp = []
        i = j = 0
        while i < m and j < len(nums2):
            if nums1[i] < nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        if j < len(nums2):
            while j < len(nums2):
                temp.append(nums2[j])
                j += 1
        if i < m:
            while i < m:
                temp.append(nums1[i])
                i += 1
        for i in range(len(temp)):
            nums1[i] = temp[i]
