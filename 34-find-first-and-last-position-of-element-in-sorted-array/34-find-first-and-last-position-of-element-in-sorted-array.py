class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0 

        end = len(nums)-1 
        if not nums:
            return [-1,-1]
        def find():
        
        

            l = start 
            r = end

            while r>=l:


                mid = (l+r)//2

                if target == nums[mid]:
                    return mid

                elif target>nums[mid]:
                    l = mid+1
                else:
                    r-=1
                    
            return -1
        if find() == -1 :
            #print('hi')
            return [-1,-1]
        
        index = find()
        
        l = r = index
        
        while l-1 >= 0 and nums[l-1] == target:
            l-=1
        while r+1 <= end and nums[r+1] == target:
            r+=1
        
        return [l,r]
        
                
        
                    
                    
                    
                
            
        
            
            
            
            