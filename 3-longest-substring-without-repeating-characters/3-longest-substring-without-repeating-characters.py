class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        '''
        string = ""
        length = 0
        for i in s:
            if i not in string:
                string += i
                
            elif i in string :
                index = string.index(i)
                string = string[index+1:]+i
                
                
            length = max(len(string),length)
        return length '''
        """
        
        last = {}
        start = 0
        length = 0
        
        for index in range(len(s)):
            if s[index] in last:
                start = max(start,last[s[index]]+1)
              
            length = max(length,index-start +1)
            
            
            last[s[index]] = index
            
        return length
        
        """
        
        ans = 0
        dic = {}
        
        
        right = 0 
        for i in range(len(s)):
            
            if s[i] not in dic:
                dic[s[i]] = i
            elif s[i] in dic:
                right = max(right,dic[s[i]] +1)
                dic[s[i]]=i
                
            ans = max(ans,i-right+1)
            
                
                
        return ans
            
        