class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open =0
        ans = 0
        for ch in s :
            if ch == '(':
                open = open + 1
            elif ch == ')':
                if open > 0:
                    open = open - 1
                else :
                    ans = ans + 1 
        return ans+open                    