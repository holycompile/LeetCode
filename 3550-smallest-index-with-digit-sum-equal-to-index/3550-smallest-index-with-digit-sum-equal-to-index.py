class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        smallestIndex=len(nums) #say for now 
        flag=False
        for i in range (len(nums)):
            value=nums[i]
            value=str(value) # nnow value is a string
            #sum of the digits to calculate
            sum=0
            for j in range(len(value)):
                sum+=int(value[j])
            if (sum == i) and (i<= smallestIndex):
                flag=True
                smallestIndex=i
            sum=0 # reassigning to zero
       
        if flag==False:
            return -1
        else:
             return smallestIndex
