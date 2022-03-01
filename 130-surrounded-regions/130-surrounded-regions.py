class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        
        
        """
        from collections import deque
        
        add_x=[0,0,1,-1]
        add_y =[1,-1,0,0]
        
        
        
        
        
        row = len(board)
        col = len(board[0])
        q = deque()
        visited =[[False for i in range(col)] for i in range(row)]
        
        for i  in range(col):
            if board[0][i] =='O':
                q.append((0,i))
                visited[0][i] = True
                
            if board[-1][i]=='O':
                q.append((row-1,i))
                visited[-1][i] = True
                
                
        for i in range(row):
            if board[i][0] =='O':
                q.append((i,0))
                visited[i][0]=True
                
            if board[i][-1]=='O':
                q.append((i,col-1,))
                visited[i][-1]=True
                
                
        while q:
            
            r,c,=q.pop()
            
            
            for i in range(4):
                coor_x = r+add_x[i]
                coor_y =c+add_y[i]
                
                
                if coor_x>=0 and coor_x<row and coor_y>=0 and coor_y<col and visited[coor_x][coor_y] == False and board[coor_x][coor_y] =='O':
                    visited[coor_x][coor_y] = True
                    q.append((coor_x,coor_y))
                    
        for r in range(1,row-1):
            for c in range(1,col-1):
                if visited[r][c] == False and board[r][c] =='O':
                    board[r][c] = 'X'
            
            
           
            
            
        
        
        