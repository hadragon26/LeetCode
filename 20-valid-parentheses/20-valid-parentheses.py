class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        dic = {"(":")",
              "{":"}",
              "[":"]"}
        
        
        
        for i in s:
            if not stack:
                if i in dic.values():
                    return False
                stack.append(i)
                
            else:
                if stack[-1] in dic and dic[stack[-1]] != i:
                    stack.append(i)
                elif stack[-1] not in dic:
                    stack.append(i)
                else:
                    stack.pop()
                    
        return not stack
                
            