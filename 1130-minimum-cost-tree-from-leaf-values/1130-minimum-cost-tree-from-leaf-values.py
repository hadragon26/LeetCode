class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        
        if len(arr) == 2:
            return arr[0]*arr[-1]
        
        
        su = 0
        
        minn = 0 
        
        
        while len(arr)>1:
            minn = min(arr)
            
            index = arr.index(minn)
            
            
            if index == 0:
                su+= minn*(arr[1])
                
            elif index == len(arr)-1:
                su+= minn*(arr[len(arr)-2])
                
            else:
                if arr[index-1]>arr[index+1]:
                    su+= minn*(arr[index+1])
                else:
                    su+= minn*(arr[index-1])
                    
            arr.remove(minn)
            
        return su
                