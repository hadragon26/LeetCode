class Solution:
    def lengthLongestPath(self, input: str) -> int:
        
        
        lst = input.split("\n")
        check = "."
        
        
        print(lst)
        
        def count_tab(string):
            return string.count("\t")
            
        
        
        
        
            
        
        
        dic = {}
       
        
        su = 0 
        for index, word in enumerate(lst):
            
            
                
                
            num = count_tab(word)
                

            #print(word,num,len(word))

            if num-1 not in dic:
                dic[num] = len(word)-num+1
            else:
                dic[num] = len(word)-num+1+dic[num-1]

            if check in word:
                su = max(su,dic[num]-1)
                    
        
        
        
        
        return su