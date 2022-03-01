class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        
        
        row = len(grid)
        add_x =[0,0,1,-1]
        add_y = [-1,1,0,0]
        col = len(grid[0])
        su = 0
        visited =[[False for i in range(col)]for i in range(row)]
        
        def dfs(x,y):
            q = deque()
            q.append((x,y))
            
            while q:
                cor_x,cor_y = q.pop()
                
                
                for i in range(4):
                    x_cor = cor_x+add_x[i]
                    y_cor = cor_y +add_y[i] 
                    
                    if x_cor >=0 and x_cor<row and y_cor>=0 and y_cor<col and visited[x_cor][y_cor] == False and grid[x_cor][y_cor] =="1":
                        q.append((x_cor,y_cor))
                        visited[x_cor][y_cor] =True
                        
            
        
        for r in range(row):
            for c in range(col):
                
                if grid[r][c] == "1" and visited[r][c] == False:
                    visited[r][c] =True
                    dfs(r,c)
                    su+=1 
                    
        return su
        