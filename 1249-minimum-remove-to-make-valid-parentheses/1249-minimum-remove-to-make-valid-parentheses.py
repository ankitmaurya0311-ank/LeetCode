class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ans = []
        for i , ch in enumerate (s):
            if ch == '(' :
                stack.append(len(ans))
                ans.append(ch)
            elif ch == ')' :
                if stack :
                    stack.pop()
                    ans.append(ch)
            else :
                    ans.append(ch)
        for i in stack :
            ans[i] = ''
        return ''.join(ans)                       