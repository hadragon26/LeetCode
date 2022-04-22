class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        dic = {}
        
        
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dic:
                return dic[(l,r)]
            
            
            if (r-l) % 2 != 0:
                even =True
            else:
                even =False
                
            if even:
                left = piles[l]
                right = piles[r]
            
            else:
                left = 0 
                right = 0 
                
            
            
            dic[(l,r)] = max(dfs(l+1,r)+left,dfs(l,r-1)+right)
            
            return dic[(l,r)]
        
        return(dfs(0,len(piles)-1)) > sum(piles)//2
    
                    
            
            
                    
        