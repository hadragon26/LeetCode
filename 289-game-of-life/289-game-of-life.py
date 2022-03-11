class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        check = copy.deepcopy(board)
        
        su =[[0 for i in range(len(check[0]))]for i in range(len(check))]
        
        
        for row in range(len(check)):
            for col in range(len(check[0])):
                
                if row-1>=0:
                    su[row][col] += check[row-1][col]
                   #print('1')
                    if col-1>=0:
                        su[row][col]+= check[row-1][col-1]
                       #print('2')
                    if col+1<len(check[0]):
                        su[row][col]+= check[row-1][col+1]
                       #print('3')
                    
                    
                    
                    
                
                if row+1<len(check):
                    su[row][col] += check[row+1][col]
                   #print('4')
                    if col-1>=0:
                        su[row][col]+= check[row+1][col-1]
                       #print('5')
                    if col+1<len(check[0]):
                        su[row][col]+= check[row+1][col+1]
                       #print('6')
                    
                    
                if col-1>=0:
                    su[row][col]+= check[row][col-1]
                    #rint('7')
                    
                if col+1<len(check[0]):
                    su[row][col]+= check[row][col+1]
                    #rint('8')
                #rint(su)
                    
                    
                if board[row][col] == 0:
                    if su[row][col] ==3:
                        board[row][col]=1
                elif board[row][col] ==1:
                    if su[row][col]>3 or su[row][col]<2:
                        board[row][col] = 0
                        
     #  print(check)
     #  print(board)
     #  print(su)
                
                