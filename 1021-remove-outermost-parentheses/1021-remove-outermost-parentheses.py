class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0 
        stack = []
        ans = ""
        for i in s:
            if count == 0:
                count +=1
                continue
            elif count ==1 and i==")":
                count -=1 
                continue
            elif i==")":
                count-=1
                ans+=i
            elif i =="(":
                count+=1
                ans+=i
                
        return ans
                
            
            