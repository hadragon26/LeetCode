class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dic = {}
        
        def dfs(s,temp,index1):
            
            if s == "":
                return True
                
            for index,ele in enumerate(s):
                temp+= ele
                
                if temp in wordDict:
                    print(temp)
                    
                    if s[index+1:]in dic and dic[s[index+1:]]==False:
                        #rint('True')
                        continue
                    
                    
                    elif dfs(s[index+1:],"",index+1) == True:
                        return True
                    
                
            dic[temp]=False
            #rint(dic)
            return False
        
                    
        if dfs(s,"",0):
            
            return True
        return False
                    
    
    
    
                
            
            
            
        