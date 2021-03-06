class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        if not firstList:
            return []
        if not secondList:
            return []
        
        
        
        i=j=0
        ans = []
        
        while i<len(firstList) and j<len(secondList):
            
            lo = max(firstList[i][0],secondList[j][0])
            hi = min(firstList[i][1],secondList[j][1])
            
            if hi>=lo:
                ans.append([lo,hi])
            
            if firstList[i][1] <= secondList[j][1]:
                i+=1
            else:
                j+=1
            
        return ans
            
        
        
        
        
        
        
        
        
        
        