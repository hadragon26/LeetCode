class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        a = [] 
        
        b = [] 
        
        
        for i in s:
            if i == "#":
                if a:
                    a.pop()
            else:
                a.append(i)
                
        for c in t:
            if c== "#":
                if b:
                    b.pop()
            else:
                b.append(c)
        
        
        return b ==a
            
            