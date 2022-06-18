class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        
        l =0
        r = l+1 
        
        while r<len(arr):
            tmp = arr[l]
            tmp2 = arr[r]
            
            #print(tmp)
            #print(arr)
            
            if tmp == 0 and r+1<len(arr):
                arr[r+1:] = arr[r:len(arr)-1]
                arr[r] = 0
                
                
                l= r+1
                r = l+1
            elif tmp == 0 and r<len(arr):
                arr[r] = 0
                
                l= r+1
                r = l+1
                
                
                
            else:
                l+=1
                r+=1
                
            
                
            