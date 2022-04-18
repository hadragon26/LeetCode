class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        
        
        ans = 0 
        
        length = len(s)
        length1 = len(t)
        
        
        for index in range(length):
            
            
            for index2 in range(length1):
                x = index
                y = index2
                d= 0 
                
                while x<length and y<length1:
                    
                    
                    if s[x]!= t[y]:
                        d+=1
                        
                    if d == 1:
                        ans +=1
                    elif d == 2:
                        break
                        
                    x+=1
                    y+=1
                        
        return ans