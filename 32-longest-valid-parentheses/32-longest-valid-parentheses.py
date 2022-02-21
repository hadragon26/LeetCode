class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        mx = 0
        
        for index,i in enumerate(s):
            if i == "(":
                stack.append(index)
            else:
                stack.pop()
                if not stack:
                    stack.append(index)
                else:
                    mx = max(index-stack[-1],mx)
                    
        return mx
            
            
            
                    
            
            