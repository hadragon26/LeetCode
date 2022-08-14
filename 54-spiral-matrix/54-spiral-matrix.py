class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        row = len(matrix)
        col = len(matrix[0])
        
        top_row = 0 
        bottom_row = row 
        
        left_col = 0 
        right_col = col
        lst = []
        while bottom_row>top_row and right_col>left_col:
            
            for track_col in range(left_col,right_col):
                
                lst.append(matrix[top_row][track_col])
                
            top_row+=1
                
            for track_row in range(top_row,bottom_row):
                
                lst.append(matrix[track_row][right_col-1])
            
            right_col-=1
                
                
            if not(left_col<right_col and top_row<bottom_row):
                break
                
            for track_col in range(right_col-1,left_col-1,-1):
                lst.append(matrix[bottom_row-1][track_col])
            
            bottom_row -=1
            
            for track_row in range(bottom_row-1,top_row-1,-1):
                
                lst.append(matrix[track_row][left_col])
            
            left_col+=1
            
            
        return lst
            
            
                
        
        
        
        
        