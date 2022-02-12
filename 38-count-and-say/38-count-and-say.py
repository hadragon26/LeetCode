class Solution:
    def countAndSay(self, n: int) -> str:
       
        
        dic = {}
        def count(n):
            
            if n ==1:
                
                return "1"
            else:
                x = count(n-1)
                ans = ""
                
                i = 0 
                st =""
                while i <len(x):
                    num =1 
                    while i< len(x)-1 and x[i] == x[i+1]:
                        i+=1
                        num+=1
                    st += str(num)+x[i]


                    i+=1
            
            
                return st
                    
                        
                        
                 
                
            
            
        return count(n)
        """  
        st =""    
        x = "1211"
        i = 0 
        while i <len(x):
            num =1 
            while i< len(x)-1 and x[i] == x[i+1]:
                i+=1
                num+=1
            st += str(num)+x[i]
            
            print(i)
            i+=1
            
            
        return st"""
                
        
                    
        