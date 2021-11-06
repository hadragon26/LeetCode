class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []
        
        
        def cal(m):
            return (m[0]**2 + m[1]**2)**(1/2)
        
        for cor in points:
        
            if len(arr)< k:
                heappush(arr,(-cal(cor),cor))
            
            
            
            elif cal(cor)>arr[0][0]:
                heappushpop(arr,(-cal(cor),cor))
                    
        
        arr1 =[]
        print(arr)
        for i in (arr[::-1]):
            arr1.append(i[-1])
        
        return (arr1)
                    
            
            
            
        
        