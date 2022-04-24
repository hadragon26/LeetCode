class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        
        
        @functools.cache
        def dp(l, m, i_am_alice): # lets return alice count
            if l == len(piles): return 0
            
            left = []
            taking_now = 0

            for x in range(2*m):
                if l+x == len(piles): break
                
                if i_am_alice:
                    taking_now += piles[l+x]
                taking_later = dp(l+x+1, max(m,x+1), not i_am_alice)
                
                left.append(taking_now + taking_later)
        
            if i_am_alice: # i want to maximize alice
                return max(left)
            
            else: # i am bob, want to minimize alice
                return min(left)
        
        return dp(0,1,True) 
            
            
        
            
            
            
            