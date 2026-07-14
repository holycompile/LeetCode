class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        starting=-1
        ending=-1
        
        if len(nums)==0:
            return [-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i]==target:
                    starting=i # taking the position
                    break # instantly break it no need to go furthur 
            for i in range(len(nums)-1,-1,-1):
                if nums[i]==target:
                    ending=i
                    break
        return [starting,ending]