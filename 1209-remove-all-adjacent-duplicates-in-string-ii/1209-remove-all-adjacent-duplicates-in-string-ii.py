class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for letter in s:
            if not stack:
                stack.append([1,letter])
            else:
                count,letter1 = stack[-1]
                if letter != letter1:
                    stack.append([1,letter])
                else:
                    count+=1
                    if count ==k:
                        stack.pop()
                    else:
                        stack[-1][0]=count
                        
        ans =""            
        for ele in stack:
            ans += ele[0]*ele[-1]
            
        return ans