class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        from collections import deque as queue
        
        
        
        
        dRow = [1,-1,0,0,-1,-1,1,1]
        dCol = [0,0,1,-1,-1,1,-1,1]
        m = len(grid)
        n = len(grid[0])
        visited = [[False for i in range(n)]for i in range(m)]
        q =queue()
        if grid[0][0] == 1:
            return -1
        if grid[m-1][n-1]:
            return -1
        
        q.append((0,0,1))
        visited[0][0] = True
        
        
        while q:
            x,y,l = q.popleft()
            
            if x==m-1 and y == n-1:
                return l
            
            
            for i in range(8):
                x1 = x+ dRow[i]
                y1 = y+dCol[i]
                
                if x1 >= 0 and y1>= 0 and x1<m and y1<n:
                    
                    if grid[x1][y1] == 0 and not visited[x1][y1]:
                        q.append((x1,y1,l+1))
                        visited[x1][y1] = True
        return -1
                    
        