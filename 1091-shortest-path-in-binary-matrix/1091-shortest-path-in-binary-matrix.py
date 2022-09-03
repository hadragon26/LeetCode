class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        visited = [[float('inf') for i in range(len(grid[0]))]for i in range(len(grid))]
        #print(float('inf')>2)
        #print(visited)
        if grid[0][0]!=0:
            return -1
        if grid[-1][-1] ==1 :
            return -1
        
        visited[0][0] = 1 
        q = []
        q.append((0,0))
        
        x_c = [1,-1,0,0,1,1,-1,-1]
        y_c = [0,0,1,-1,1,-1,-1,1]
        
        while q:
            
            row,col = q.pop(0)
            path = visited[row][col]
            
            for i in range(8):
                x_t = row + x_c[i]
                y_t = col + y_c[i]
                
                
                if 0 <= x_t < len(grid) and 0<= y_t<len(grid[0]) and grid[x_t][y_t] == 0:
                    
                    if visited[x_t][y_t] > path+1:
                        visited[x_t][y_t] = path+1

                        q.append((x_t,y_t))
            
        
        if visited[-1][-1] == float('inf'):
            return -1
        return visited[-1][-1]
        
        
                    
        