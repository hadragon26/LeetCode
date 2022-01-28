
class Solution:
    def frequencySort(self, s: str) -> str:
        
        dic = {}
        
        for letter in s:
            if letter not in dic:
                dic[letter] = 1
            else:
                dic[letter]+= 1
                
        heap = []
        
        
        for key,value in dic.items():
            heappush(heap,(-value,key))
        string = ""  
        print(heap)
        while heap:
            ele = heappop(heap)
            string += ele[1]*-ele[0]
            
            
        return string
        