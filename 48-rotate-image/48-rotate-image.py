class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        row = len(matrix)
        col = row
        start = 0 
        end = row -1 
        diff = 0 
        
        while end>start:
        
            top = matrix[start][start:end+1]
            left = [matrix[i][start] for i in range(start,end+1)]
            bottom = matrix[end][start:end+1]
            right = [matrix[i][end] for i in range(start,end+1)]

            matrix[start][start:end+1] = left[::-1]
            matrix[end][start:end+1] = right[::-1]
            for i in range(start,end+1):
                matrix[i][start] = bottom[i-diff]
                matrix[i][end] = top[i-diff]
                
                
            
            diff +=1
                
            start +=1
            end -=1 
        
        
        
        
        