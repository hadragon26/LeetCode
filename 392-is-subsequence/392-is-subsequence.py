class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True
        
        length = len(s)
        n= 0 
        track = 0 
        
        while track < len(t):
            if s[n] == t[track]:
                n+=1
            if n == length:
                return True
                
            
            track+=1
            
        return False
        
        