class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        
        com = '->'
        
        
        
        ans = [] 
        temp = []
        final = []
        
        sin = True
        
        for index in range(len(nums)):
            if index==0:
                temp.append(nums[index])
                temp.append(nums[index])
                start_index = index
                sin = False
                ans.append(temp)
                
                
            else:
                if index !=0 and nums[index] - nums[start_index] == index-start_index:
                    ans[-1][-1] = nums[index]
                
                else:
                    temp = []
                    temp.append(nums[index])
                    temp.append(nums[index])
                    start_index = index
                    ans.append(temp)
                
                
                
            
        
        
        
                
            
        for i in ans:
            if i[0] == i[-1]:
                final.append(str(i[0]))
            else:
                string = str(i[0])+'->'+str(i[-1])
                final.append(string)
        return final
                
                
            
            