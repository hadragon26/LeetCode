class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        
        nums.sort()
        lst = []
        
        for i in range(len(nums)):
            if i!= 0 and nums[i-1] == nums[i]:
                continue
            
            l1 = i
            
            for x in range(i+1,len(nums)):
                if x!= i+1 and nums[x-1] == nums[x]:
                    continue
                l2 = x
                
                l3 = x+1
                
                r = len(nums)-1
                
                while r>l3:
                    
                    if nums[l1] + nums[l2] + nums[l3] + nums[r] <target:
                        l3 +=1
                    elif nums[l1] + nums[l2] + nums[l3] + nums[r] >target:
                        r-=1
                    else:
                        lst.append([nums[l1],nums[l2],nums[l3],nums[r]])
                        
                        l3+=1
                        r-=1 
                        
                        while r>l3 and nums[l3-1] == nums[l3]:
                            l3+=1
                        while r>13 and nums[r+1] == nums[r]:
                            r-=1
                            
        return lst
                    
                
                
        

