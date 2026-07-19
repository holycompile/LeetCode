class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        length=len(nums) # taking the length 
        expected_sum=0
        what_we_get=0
        for i in range(length+1):
            expected_sum+=i
        for i in nums:
            what_we_get+=i
        return (expected_sum - what_we_get)
        
        
        