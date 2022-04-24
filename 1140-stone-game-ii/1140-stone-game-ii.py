class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @functools.cache
        
         
        
        def take(l,M,play):
            if l== len(piles):
                return 0
        
            left = []
            su = 0 
            for i in range(2*M):
                
                if l+i>= len(piles):
                     
                    break
                
                if play:
                    su+= piles[l+i]
                taking_later = (take(l+i+1,max(M,i+1),not play))
                left.append(su+taking_later)
            if play:
                return max(left)
            else:
                return min(left)

            
        
        return take(0,1,True)
    
   
            
            
        
            
            
            
            