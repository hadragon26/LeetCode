# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        
        if not subRoot:
            return True 
        if not root:
            return False
        
        def isSame(i,r):
            
            if not i and not r:
                return True
            
            if i and r and i.val == r.val:
                
                return isSame(i.right,r.right) and isSame(i.left,r.left)
            
            return False
        
        q = []
        
        q.append(root)
        
        while q:
            node = q.pop(0)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
            if node.val == subRoot.val:
                if isSame(node,subRoot):
                    return True
                
        return False
        
            
        
        
        