class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = "" 
        
        def find(x,y):
            left =x 
            right = y
            
            while left>= 0 and right < len(s) and s[left] == s[right]:
                left -=1 
                right +=1 
                
            return s[left+1:right]
        
        for i in range(len(s)):
            
            odd = find(i,i)
            even = find(i,i+1)
            
            if len(res) < len(odd):
                res = odd
            if len(res)<len(even):
                res = even
            
            
            
            
            
        return res
            
        
            