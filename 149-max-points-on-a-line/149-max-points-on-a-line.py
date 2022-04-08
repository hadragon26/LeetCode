class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        dic ={}
        
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                
                if (points[j][0]-points[i][0]) == 0:
                    slop = float('inf')
                else:
                
                    slop = (points[j][1]-points[i][1])/(points[j][0]-points[i][0])
                
                if (i,slop) in dic:
                    dic[(i,slop)]+=1
                else:
                    dic[(i,slop)]=1
                    
                    
                
                    
        if dic.values():
            
            return max(dic.values())+1
        
        return 1
                    
                
                
                
                
                
                
                
                
                
                