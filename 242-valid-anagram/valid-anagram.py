class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        #simply sorting both s and t
        s=s.lower()
        t=t.lower()
        #making sure they all are in lower case 
        new_s=""
        new_t=""
        for i in range(97,123):
            for j in s:
                if chr(i)==j:
                    new_s+=j
            for j in t:
                if chr(i)==j:
                    new_t+=j
        if new_s==new_t:
            return True
        else:
            return False
        