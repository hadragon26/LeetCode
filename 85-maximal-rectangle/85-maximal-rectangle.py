class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        dic = {}
        
        for row in range(len(matrix)):
            
            if row == 0:
                dic[row] = list(map(int,matrix[0]))
                
            else:
                temp = dic[row-1]
                b = temp.copy()
                for index,i in enumerate(matrix[row]):
                    if i== "1":
                        b[index] += 1
                    else:
                        b[index] = 0 
                        
                dic[row] = b
                
        area  = 0
        length = len(matrix[0])
        
        
        
        for i in dic:
        
        
        
        
        
        
        
            stack = []

            for index,height in enumerate(dic[i]):


                if not stack:

                    stack.append((index,height))
                else:
                    top = stack[-1][-1]

                    if height>= top:
                        stack.append((index,height))

                    else:
                        
                        start = index

                        while stack and stack[-1][1] > height:

                            index1,height1 = stack.pop()

                            area = max(area,height1*(index-index1))

                            start = index1



                        stack.append((start,height))

            
            for ele in stack:
                area = max(area,ele[-1]*(length-ele[0]))

        return area
                
                
        
                    
        