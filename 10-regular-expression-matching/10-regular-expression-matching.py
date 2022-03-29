class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        
        dic ={}
        def dfs(i,j):
            if (i,j) in dic:
                return dic[(i,j)]
            
            if i >=len(s) and j>=len(p):
                return True
            if j>=len(p):
                return False
            
            if i <len(s):
            
                match = s[i]==p[j] or p[j] == '.'
                
                
            else:
                match = False
            if j+1<len(p) and p[j+1]=="*":
                dic[(i,j)] = dfs(i,j+2) or match and dfs(i+1,j)
                return(dfs(i,j+2) or match and dfs(i+1,j))
                
            if match:
                dic[(i,j)] = dfs(i+1,j+1)
                return dfs(i+1,j+1)
            
            return False
        
        return dfs(0,0)
                        
            
            
            
        