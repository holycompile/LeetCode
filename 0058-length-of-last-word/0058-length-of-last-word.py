class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip() # removiong leading and trailing spaces
        s=" "+s # in case its a 1 word string 
        # we just need the length of the last word right no matter the sequence we are counting or what
        freq=0
        for i in range(len(s)-1, -1, -1):
            if s[i]==" ":
                break
            else:
                freq+=1
            
        return freq
