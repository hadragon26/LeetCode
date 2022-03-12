class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        least = matrix[0][0]
        most = matrix[-1][-1]
        
        
        if target < least or target > most:
            return False
        
        col = len(matrix[0])-1
        row = 0
        while row<len(matrix) and col>= 0:
            if target< matrix[row][col]:
                col-=1
                
            elif target>matrix[row][col]:
                row += 1
                
            else:
                return True
            
        return False