class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        from collections import deque
        
        col = len(matrix[0])
        row = len(matrix)
        
        visit = [[False for i in range(col)] for i in range(row)]
        
        print([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
        
        
        ans = [] 
        track = deque()
        track.append((0,0,'right'))
        
        
        while track:
            r,c,d = track.pop()
            
            if d == 'right':
            
                if c+1<col and not visit[r][c+1]:
                    track.append((r,c+1,d))
                elif r+1<row and not visit[r+1][c]:
                    track.append((r+1,c,'down')) 
            elif d == 'down':
                if r+1<row and not visit[r+1][c]:
                    track.append((r+1,c,d)) 
                
                elif c-1>=0 and not visit[r][c-1]:
                    track.append((r,c-1,'left'))
            elif d == 'left':
                if c-1>=0 and not visit[r][c-1]:
                    track.append((r,c-1,d))
                elif  r-1>=0 and not visit[r-1][c]:
                    track.append((r-1,c,'up'))
                    
            elif d == 'up':
                if  r-1>=0 and not visit[r-1][c]:
                    track.append((r-1,c,d))
                elif c+1<col and not visit[r][c+1]:
                    track.append((r,c+1,'right'))
                    
                
                
                
                
                
           
            ans.append(matrix[r][c])
            visit[r][c] =True
            
        return ans
                
            
            