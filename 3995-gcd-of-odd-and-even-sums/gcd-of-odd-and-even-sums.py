
from fractions import gcd
class Solution(object):
    def gcdOfOddEvenSums(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        #sum of 1st 4 odd numbers 
        k=1
        q=2
        sumOdd=0
        sumEven=0
        for i in range(n):
            sumOdd+=k
            k=k+2
            sumEven+=q
            q=q+2
        return gcd(sumOdd, sumEven)
        

