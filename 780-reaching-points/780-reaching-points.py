class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        if tx<sx or ty<sy:
            return False
        
        if tx ==sx:
            
            return (ty-sy)%sx == 0
        
        if ty == sy:
            
            return (tx-sx)%sy == 0
        
        while tx>sx and ty>sy:
            
            if tx>ty:
                tx = tx%ty
                
            elif ty>=tx:
                ty = ty%tx
                
                
        if tx ==sx:
            
            return (ty-sy)%sx == 0
        
        if ty == sy:
            
            return (tx-sx)%sy == 0
        
        return False
                
        
        
        
            
            
            
        