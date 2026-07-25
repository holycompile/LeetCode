class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        j=len(s)
        for i in range(1,j+1):
            if i<j:
                swap=s[i-1]
                s[i-1]=s[j-1]
                s[j-1]=swap
                j=j-1
