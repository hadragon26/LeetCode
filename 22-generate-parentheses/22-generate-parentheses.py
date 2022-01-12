class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        
        
        
        def backtrack(start,close,string):
            if len(string) == n*2:
                res.append(string)
            
            if start<n:
                backtrack(start+1,close,string+"(")
            if close<start:
                backtrack(start,close+1,string+")")
                
        backtrack(0,0,"")
        
        return res