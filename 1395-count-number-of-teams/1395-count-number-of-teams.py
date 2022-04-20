class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        
        right = [0 for i in range(len(rating))]
        left = [0 for i in range(len(rating))]
        
        res = 0
        for i in range(1,len(rating)):
            
            ele = rating[i]
            for j in range(i):
                if ele > rating[j]:
                    left[i]+=1
                    
        for i in range(len(rating)-2,-1,-1):
            
            ele = rating[i]
            #rint(ele)
            for j in range(len(rating)-1,i,-1):
                #rint('index'+ '' +str(j))
                #rint(rating[j])
                if ele> rating[j]:
                    right[i]+=1 
                    
                    
        for i in range(1,len(rating)):
            
            ele = rating[i]
            for j in range(i):
                if ele > rating[j]:
                    res+= left[j]
                    
        for i in range(len(rating)-2,-1,-1):
            
            ele = rating[i]
            #rint(ele)
            for j in range(len(rating)-1,i,-1):
                #rint('index'+ '' +str(j))
                #rint(rating[j])
                if ele> rating[j]:
                    res+= right[j]
                    
        return res
                    
                    
        
            