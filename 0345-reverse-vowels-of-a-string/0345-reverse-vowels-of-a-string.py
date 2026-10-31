class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        list=[] # empty list
        # 1st what we are doing is to find those vowels 
        # Store those vowels and then replcae with '#'

        for i in range (len(s)):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                list.append(s[i])
                s=s[0:i]+'#'+s[(i+1):]
        # Now we will reverse the list 
        list.reverse()
        #Now integratinig the # with the list items one by one 
        p=0
        for i in range (len(s)):
            if s[i]=='#' and p < len(list):
                s=s[0:i]+(list[p])+s[(i+1):]
                p+=1
        return s
        