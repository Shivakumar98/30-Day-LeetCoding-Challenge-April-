Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 

Input: 19
Output: true
Explanation: 
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1



class Solution:
    def isHappy(self, n: int) -> bool:
    
        seen=set()
        
        while self.sqnum(n) not in seen:
            s=self.sqnum(n)
            if s==1:
                return True
            else:
                n=s
                seen.add(n)
        return False
        
    def sqnum(self,n):
        res=0
        while n>0:
            rem=n%10
            res+=rem*rem
            n=n//10
        return res
