class Solution:
    def numSquares(self, n: int) -> int:
        
        
        
        
        lst = []
        
        for i in range(1,floor(n**(1/2))+1):
            lst.append(i**2)
            
        
        dp = [n] *(n+1)
        dp[0] = 0
        
        for i in range(1,n+1):
            for square in lst:
                if i-square<0:
                    break
                dp[i] = min(dp[i],1+dp[i-square])
                
                
        return dp[n]