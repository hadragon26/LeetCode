class Solution:
    def maximum69Number (self, num: int) -> int:
        
        ans = ""
        
        
        for index,ele in enumerate(str(num)):
            if ele == "6":
                ans+="9"
                ans+= str(num)[index+1:]
                break
            else:
                ans+="9"
                
        return int(ans)
                
            