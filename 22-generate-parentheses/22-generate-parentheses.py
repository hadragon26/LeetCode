class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        
        
        
        def backtrack(res,start,close,string):
            if len(string) == n*2:
                res.append(string)
            
            if start<n:
                backtrack(res,start+1,close,string+"(")
            if close<start:
                backtrack(res,start,close+1,string+")")
            return res
        
        return backtrack([],0,0,"")
        
        