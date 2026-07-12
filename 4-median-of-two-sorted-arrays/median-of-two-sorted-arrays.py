class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #say nums1=[1,3] and nums2=[2]
        merge_array=[] # let it be empty 1st 
        #1st lets merge it 
        m= len(nums1)
        n= len(nums2)
        for i in range (m):
            merge_array.append(nums1[i])
        for i in range (n):
            merge_array.append(nums2[i])
        #sorting using bubble sort
        length=len(merge_array)
        for i in range(length-1):
            for j in range(length-1-i):
                if merge_array[j]>merge_array[j+1]:
                    swap=merge_array[j]
                    merge_array[j]=merge_array[j+1]
                    merge_array[j+1]=swap
        #finding the meadian 
        # finding the median
        if length % 2 == 0:      # even number of elements
            median = (merge_array[(length // 2) - 1] + merge_array[length // 2]) / 2.0
        else:                    # odd number of elements
            median = merge_array[length // 2]

        return median
