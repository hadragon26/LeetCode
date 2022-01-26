class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        
        if target >= letters[-1] or target <letters[0]:
            return letters[0]
        
        start = 0 
        end = len(letters) -1 
        
        while end >= start :
            mid = (end+start)//2
            
            
            
            if target >= letters[mid]:
                start = mid + 1
            
            elif target < letters[mid]:
                end = mid - 1
                
        return letters[start]
        
        
        