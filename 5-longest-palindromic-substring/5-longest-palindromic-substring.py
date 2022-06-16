class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return 
        
        
        def check(index):
            
            ans = s[index]
            temp = s[index]
            l= index
            r = index
            
            while l>=0 and r<len(s) and s[l] == s[r]:
                ans = s[l:r+1]
                l-=1 
                r+=1 
                
                
            l = index
            r = index+1
            if r<len(s) and s[r]==s[l]:
                temp = s[l:r+1]
            length = len(ans)
            
            while l>=0 and r<len(s) and s[l] == s[r]:
                temp = s[l:r+1]
                l-=1 
                r+=1 
               
                
            if length<len(temp):
                
                ans = temp
                
            return ans
        
        ma = 0 
        ans = s[0]
            
        for i in range(len(s)):
            if len(check(i)) > ma:
                ma = len(check(i))
                ans = check(i)
        return ans
            
            
            
                
            
        
            