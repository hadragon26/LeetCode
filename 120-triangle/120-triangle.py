class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if not triangle:
            return
        
        if len(triangle) == 1:
            return triangle[0][0]
        
        
        
        dic = {}
        
        ma = float('inf')
        
        
        for row in range(len(triangle)):
            
            if row == 0:
                dic[(0,0)] = triangle[0][0]
                continue
            
            for col in range(len(triangle[row])):
                
                if col != 0 and col != len(triangle[row]) -1 :
                
                    dic[(row,col)] = min(triangle[row][col] + dic[(row-1,col)] ,triangle[row][col]+dic[(row-1,col-1)])
                elif col == 0 :
                    dic[(row,col)] = triangle[row][col] + dic[(row-1,col)]
                elif col == len(triangle[row]) - 1:
                    dic[(row,col)] = triangle[row][col] + dic[(row-1,col-1)]
                    
                    
                    
                
                    
                
                if row ==len(triangle)-1:
                    
                    ma = min(dic[(row,col)],ma)
                    
                    
        return ma
            