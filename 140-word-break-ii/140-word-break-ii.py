class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        
        dic = {}
        lst = []
        
        
        
        def dfs(s,temp,index1,word):
            
            if s =="":
                lst.append(word)
                
                
                
                
                
                
            for index,ele in enumerate(s):
                temp += ele
                
                if temp in wordDict:
                    dfs(s[index+1:],'',index+1,word+" "+temp)
                        
                        
            
            
            
            
        dfs(s,"",0,"")
        
        for i in lst:
            ans.append(i[1:])
            
        return ans
                        
                        
            
                
                
        
        
        