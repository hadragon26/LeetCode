class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        left = 0
        mrc = 0
        l = 0
        
        
        for index,char in enumerate(s):
            
            if char not in dic:
                dic[char] =1 
            elif char in dic:
                dic[char]+=1
                
            mrc = max(mrc,dic[char])
            
            
            while index - left + 1 - mrc > k:
                dic[s[left]]-=1
                left+=1
                    
            l = max(l,index-left+1)
        
                    
        return l
                    
            
                
                
            