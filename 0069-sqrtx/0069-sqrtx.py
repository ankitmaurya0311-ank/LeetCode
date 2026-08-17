class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2 :
            return x
        l= 2
        r = x//2
        ans = 1
        while l <= r :
            m = l+(r-l)//2
            nums = m * m 
            if nums == x:
                return m
            if nums < x:
                ans = m
                l=m+1
            else :
                r = m-1
        return ans                 
        