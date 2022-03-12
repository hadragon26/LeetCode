# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        playing =True
        
        def check(root,small,big):
            
            if not root:
                return True
            
            elif root.val<= small or root.val>=big:
                return False
            else:
                
                
            
                return check(root.left,small,min(big,root.val)) and check(root.right,max(small,root.val),big)
            
        return check(root,float('-inf'),float('inf'))
        
            
        
            
            
            
            