class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        from collections import deque
        x= [0,0,-1,1]
        y = [1,-1,0,0]
        row = len(board)
        
        col = len(board[0])
        
        path = set()
        
        def dfs(x,y,letter):
            if letter == len(word):
                return True
            if (x,y) in path or x< 0 or x>=row or y<0 or y>=col or board[x][y] != word[letter]:
                return False
            
            path.add((x,y))
            res = dfs(x+1,y,letter+1) or dfs(x-1,y,letter+1) or dfs(x,y+1,letter+1) or dfs(x,y-1,letter+1)
            path.remove((x,y))
            
            return res
        
        
        
        for i in range(row):
            for j in range(col):
                
                if dfs(i,j,0):
                    return True
                
        return False
    
    
        
                    
                    
                
        
        
        