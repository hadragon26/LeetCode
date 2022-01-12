class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        res = [""]
       
        
        for index,ele in enumerate(s):
            
            if ele.isdigit():
                for i in range(len(res)):
                    res[i]+=ele
            else:
                temp = res[:]
                for i in range(len(res)):
                    res[i]+=ele
                    temp[i] += ele.swapcase()
                res.extend(temp)
        return res
                
                
        """
        ans = ""
        def dfs(i):
            
            if i == len(s):
                res.append(ans)
            ans+=s[i]
            dfs(i+1)
            
            while i>0 and s[]
        """
                
            
            
                
            
                
        