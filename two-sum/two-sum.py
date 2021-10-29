class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        new_list =[]
        index  = 0 
        index1 = 0 
        ans = []
        for num in nums:
            
            new_list.append(num)
            dic[index] = target - num
                
            for k,v in dic.items():
                if v == num and k!=index:
                    index1 = index
                    ans = [k,index1]
                        
                    
            
            
            index += 1 
        
      
            
                
        return ans
            
            
        