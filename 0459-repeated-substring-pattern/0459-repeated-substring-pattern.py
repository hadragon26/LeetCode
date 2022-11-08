class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        
        
        length = len(s)
        #print(s[0:1]*3)
        for index in range(length-1):
            if length % (index+1) == 0 :
                if s[:index+1]*(length//(index+1)) == s:
                    print(s[:index+1])
                    return True
                
        return False