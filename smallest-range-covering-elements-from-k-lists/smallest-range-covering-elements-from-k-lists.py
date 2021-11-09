class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        track = []
        
        
        ans = []
        final = []
        
        for i,lst in enumerate(nums):
            heappush(track,(lst[0],0,lst,i))
            ans.append(lst[0])
            
        final.append(min(ans))
        final.append(max(ans))
        thres = final[-1] -final[0]
        
        while track:
            
            ele,index,grp,k = heappop(track)
            
            index+= 1 
            
            if index < len(grp):
                ans[k] = grp[index]
                heappush(track,(grp[index],index,grp,k))
                        
            d = max(ans) - min(ans)
            
            
            
            if d<thres:
                thres = d
                final[0]=min(ans)
                final[1] =max(ans)
                
                
        return(final)
                
            
                
            