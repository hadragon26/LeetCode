class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        
        ma = days[-1]
        
        track = [float('inf') for i in range(ma+1)]
        track[0] = 0 
        day = [1,7,30]
        for index in range(1,ma+1):
            if index not in days:
                track[index]=track[index-1]
                continue
            for i in range(3):
                
                if index-day[i]>=0 :
                    track[index]=min(track[index],track[index-day[i]]+costs[i])
                    
                else:
                    track[index] = min(track[index],costs[i])
                    
        return track[-1]
                