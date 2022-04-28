class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        
        
        
        row = len(heights)
        col = len(heights[0])
        
        track = [[True for i in range(col)]for i in range(row)]
        
        check = []
        
        xc = [1,-1,0,0]
        yc = [0,0,-1,1]

        
        heappush(check,(0,0,0))
        track[0][0]=False
        res = 0 
        
        ans = 0 
        while check:
            diff,x,y = heappop(check)
            
            res = max(diff,res)
            
            
            ele = heights[x][y]
            if x == row-1 and y ==col-1:
                return res
            track[x][y] = False
            for i in range(4):
                tx = x+xc[i]
                ty = y+yc[i]
            
                
                
                if tx>=0 and tx<row and ty>=0 and ty<col and track[tx][ty]:
                    d= abs(heights[tx][ty]-ele)
                    heappush(check,(d,tx,ty))
                    #print(d,tx,ty)
            
                    
            
        
        
        