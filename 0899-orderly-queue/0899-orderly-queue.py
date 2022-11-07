class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        
        
        if k>=2:
            
            s =list(s)
            s.sort()
            return "".join(s)
        
        if k ==1:
            
            ans = s
            index = 1
            while index< len(s):
                
                    
                temp = s[index:] + s[0:index] 
                ans = min(ans,temp)
                index+=1
            return ans
            