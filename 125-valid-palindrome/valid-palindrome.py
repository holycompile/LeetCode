class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        # remvoing all the alpha numeric characters 
        copy=""
        for i in range(len(s)):
            if s[i].isalnum():
                copy+=s[i]
        reverse=""
        for i in range(len(copy)-1, -1, -1):
                reverse+=copy[i]
        if reverse==copy:
            return True
        else:
            return False
    

        