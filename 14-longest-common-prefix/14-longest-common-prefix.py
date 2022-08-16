class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        if len(strs)==1:
            return strs[0]
        
        i = 1 
        strs.sort(key=len)
        while True:
        
            check = strs[0][0:i]
            
        
        
            for word in strs[1:]:
                if check!= word[:i]:
                    return word[:i-1]
                    
            i+=1
            
            if i >len(strs[0]):
                return strs[0]
            
            
            
        
            
            
        
                
        