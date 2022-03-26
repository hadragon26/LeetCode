class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        dic = {}
        
        for i in nums:
            dic[i] = 1
            
        dic1 ={}
        ans =0 
        for i in dic:
            if i+1 not in dic:
                dic1[i] = 1
                
                ans = max(ans,1)
                
            elif i+1 in dic and dic[i]!='False':
                count =1 
                x = i
                
                while i+1 in dic:
                    if i+1 not in dic1:
                        dic[i+1] ='False'
                        count +=1
                        i = i+1
                    elif i+1 in dic1:
                        dic[i+1] ='False'
                        count +=dic1[i+1]
                        i = i+1
                        break
                            
                dic1[x] = count
                ans =max(ans,count)
        #print(dic)
        #print(dic1)
                
        return ans
                
            