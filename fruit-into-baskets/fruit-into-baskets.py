class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left, fruits_picked, basket = 0, 0, set()
        
        for right in range(len(fruits)):
            
            if len(basket) < 2 and fruits[right] not in basket: 
                basket.add(fruits[right])

            elif fruits[right] not in basket:
                basket = {fruits[right-1], fruits[right]} 
                #when we encounter a new fruit type we add it 
                # and the fruit type before it, 
                # essentially removing the first fruit type
                
                left = right - 1 
                while fruits[left] == fruits[left-1]: 
                    #now we check if previous indexs also has the same 
                    # fruit type so we count them as well
                    left -= 1
            
            fruits_picked = max(fruits_picked, right - left + 1) 
            #length of curr window will be num of fruits picked
        
        return fruits_picked
            
                
                
                
                
            
            
            
        