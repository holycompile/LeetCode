class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = []

        for i in nums1:
            for j in nums2:
                if i == j:
                    intersection.append(i)
                    nums2.remove(j)      # Remove the matched element
                    break                # Stop searching for this i

        return intersection
