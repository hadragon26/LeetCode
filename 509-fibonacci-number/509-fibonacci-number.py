class Solution:
    def fib(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        if n == 0:
            return 0 
        if n ==1 :
             return 1 
        
        dp[0],dp[1] = 0,1
        
        i =2 
        
        while i <= n:
            dp[i] = dp[i-1]+dp[i-2]
            i+=1
            
        return dp[-1]