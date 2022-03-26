class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        
        
        def check(l,r):
            
        
            while r>l:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
                    
            return True
            
        def dfs(i):
            
            if i >= len(s):
                res.append(path.copy())
                return 
            for j in range(i,len(s)):
                if check(i,j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
                    
            return res
        
        return dfs(0)
                    