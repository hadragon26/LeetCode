class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        
        if sx> tx or sy >ty:
            return False
        
        if sx == tx:
            return (ty-sy) % sx == 0
        elif sy ==ty:
            return (tx-sx)% sy == 0 
        
        while tx>sx and ty>sy:
            
            if tx>ty:
                tx = tx%ty
            else:
                ty = ty%tx
                
        if sx == tx:
            return (ty-sy) % sx == 0 
        elif sy ==ty:
            return (tx-sx)% sy == 0
        
        return False
        
        
        
            
            
            
        