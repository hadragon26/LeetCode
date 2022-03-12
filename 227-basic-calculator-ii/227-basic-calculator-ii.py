class Solution:
    def calculate(self, s: str) -> int:
        stack = deque()
        
        s= re.sub(r"\s+", "", s)
        index = 0 
        
        while index<len(s):
            
            
            if s[index] == '/' :
                num = int(stack.pop())
                index+=1
                temp =""
                while index<len(s) and s[index].isdigit():
                    
                    temp += s[index]
                    index+=1
                cal = floor(num/int(temp))
                stack.append(str(cal))
                
                
            elif s[index] =='*':
                num = int(stack.pop())
                index+=1 
                temp = ""
                while index<len(s) and s[index].isdigit():
                    
                    temp += s[index]
                    index+=1
                cal = num * (int(temp))
                stack.append(str(cal))
                
                
            
            else:
                temp = ''
                while index<len(s) and s[index].isdigit():
                    temp += s[index]
                    index+=1 
                if temp =="":
                    temp += s[index]
                    index+=1 
            
                stack.append(temp)
                
                
        #print(stack)       
        #print(int(0))
        ans = 0 
        neg =False
        while stack:
            
            ele = stack.popleft()
            #print(ele)
            
            if ele =='-':
                neg =True
                continue
            if ele =='+':
                continue
            
            elif neg:
                ans-=int(ele)
                
                neg=False
            else:
                ans += int(ele)
                
        return ans
                
            
            
            
            
            
            