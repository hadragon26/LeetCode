class Solution:
    def reverseVowels(self, s: str) -> str:
        
        
        lst = []
        vowel = ['a','e','i','o','u','A','E',"I",'O',"U"]
        track = []
        for letter in s :
            
            lst.append(letter)
            if letter in vowel:
                track.append(letter)
                
                
        if not track:
            return s 
                
        for index , letter in enumerate(lst):
            if letter in vowel:
                lst[index]=track.pop()
                
        
        return("".join(lst))
                
                
            
            
            
        