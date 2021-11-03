class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        if ord(target)>= ord(letters[-1]):
            return letters[0]
        
        start = 0 
        
        end = len(letters)-1
        
        while end>=start:
            
            mid = (start + end)//2
            
            
            if letters[mid] == target:
                while mid<len(letters)-1 and letters[mid] == letters[mid+1]:
                    mid+=1
                return letters[mid+1]
            
            if ord(letters[mid])< ord(target):
                start = mid+1
                
            elif  ord(target) < ord(letters[mid]):
                end = mid-1
                
        return letters[start]
            
            