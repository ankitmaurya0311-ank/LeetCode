class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        num = 0 
        for ch in s :
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[' :
                stack.append((ans , num))
                ans = '' 
                num = 0
            elif ch == ']' :
                prev_str , repeat = stack.pop()
                ans = prev_str + ans * repeat 
            else :
                ans += ch
        return ans                    

        