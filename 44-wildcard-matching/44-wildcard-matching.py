class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        dic = {}
        
        
        def find(i,g):
            #print(i,g)
            if (i,g) in dic:
                return dic[(i,g)]
            if i >= len(s) and g>=len(p):
                return True
            if g>=len(p):
                return False
            
            
            if  i<len(s):
        
        
                match = s[i] == p[g] or p[g]=='?' or p[g] =='*'
            
            else:
                match = False
            
            if p[g]=='*':
                dic[(i,g)] = find(i,g+1) or match and find(i+1,g) 
                return (find(i,g+1) or match and find(i+1,g) )
            
            
            if match:
                dic[(i,g)] = find(i+1,g+1)
                return find(i+1,g+1)
            
            
            
            
            return False
        
        
        return find(0,0)
            