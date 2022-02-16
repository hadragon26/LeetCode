class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        
        first_row = obstacleGrid[0]
        
        playing = False 
        for i in range(n):
            if playing:
                first_row[i] = 0 
            elif first_row[i] == 0:
                first_row[i] = 1
            else:
                first_row[i] = 0
                playing = True
                
        
        d1 = first_row
        d2 = [0]*n
        
        
        row = 1 
        while row <m:
            
            for i in range(n):
                if obstacleGrid[row][i] == 1:
                    continue
                elif i == 0:
                    d2[i] = d1[i]
                else:
                    d2[i]  = d2[i-1] + d1[i]
            row += 1 
            d1 = d2
            d2 =[0]*(n)
       
        return d1[n-1]
            
        
            
            
            
            
            
        
        
        
        