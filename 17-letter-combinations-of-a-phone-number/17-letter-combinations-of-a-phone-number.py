class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        dic = {
            
            "2":["a","b","c"],
            "3" : ["d","e","f"],
            "4": ["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        
        
        lst = [] 
        
        for i in digits:
            if not lst:
                lst.extend(dic[i])
                
            else:
                
                new_lst = []
                
                for ele in lst:
                    for x in dic[i]:
                        new_lst.append(ele+x)
                lst = new_lst
                
                
        return lst

        
        