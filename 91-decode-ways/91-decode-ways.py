class Solution:
    def numDecodings(self, s: str) -> int:
        
        
        
        dp = [0 for i in range(len(s)+1)]
        
        dp[0] = 1
        
        if s[0] == "0":
            dp[1] = 0
            return 0
        else:
            dp[1] =1
            
            
        for i in range(2,len(s)+1):
            
            one = s[i-1:i]
            two = s[i-2:i]
            
            
            if int(one)>= 1:
                dp[i] += dp[i-1]
            
            if 10 <= int(two) <= 26:
                dp[i] += dp[i-2]
                
                
        return dp[len(s)]
            
                        
                        
            
                
                
                
            
        
            
            
        
        
        
        
        