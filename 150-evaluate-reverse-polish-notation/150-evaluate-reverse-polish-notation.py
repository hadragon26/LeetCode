class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        stack = []
        
        check = ['+','-','*','/']
        
        
        
        
        for i in tokens:
            
            if i in check:
                if i==check[0]:
                    stack.append(stack.pop()+stack.pop())
                elif i == check[1]:
                    x = stack.pop()
                    y = stack.pop()
                    stack.append(y-x)
                elif i == check[2]:
                    stack.append(stack.pop()*stack.pop())
                elif i == check[3]:
                    x = stack.pop()
                    y = stack.pop()
                    
                    if y/x < 0:
                        ans = ceil(y/x)
                    else:
                        ans = floor(y/x)
                    stack.append(ans)
                    
            else:
                    
                stack.append(int(i))
                
            #print(stack)
        return stack[-1]
                
                    
        
        
        
        