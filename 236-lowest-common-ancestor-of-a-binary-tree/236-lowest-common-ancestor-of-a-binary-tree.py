# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        
        def check(root):
            
            if not root:
                return 
            
            
            if root.val ==q.val or root.val ==p.val:
                return root
            
            
            
            
            
            left = check(root.left)
            right = check(root.right)
            
            if left and right:
                return root
            
            if not left:
                return right
            else:
                return left
            
        return check(root)
        