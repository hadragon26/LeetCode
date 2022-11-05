class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        
        if not fruits:
            return 0
        if len(fruits) == 1:
            return 1 
        dp =  [[0,0] for i in range(len(fruits))]
        
        
        dp[0] = [1,1]
        track = []
        track.append(fruits[0])
        su = 0 
        length = 1
        for index, ele in enumerate(fruits):
            
            count = dp[index-1][0]
            consec = dp[index-1][1]
            if index == 0:
                continue
            if ele == fruits[index-1]:
                dp[index] = [count+1,consec+1]
            
            elif ele in track:
                
                dp[index] =[count+1,1]
                    
                    
                    
                    
                    
            elif ele not in track :
                if length == 1:
                    
                    
                    dp[index] = [count+1,1]
                    track.append(ele)
                    length += 1 
                else:
                    dp[index] = [consec+1,1]
                    track = [ele,fruits[index-1]]
            
            su = max(su,dp[index][0])
                    
        #print(dp)    
                    
        return su
            
            
            