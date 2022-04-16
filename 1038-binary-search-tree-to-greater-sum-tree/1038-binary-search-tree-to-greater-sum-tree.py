# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        
        self.su = 0
       
        def change(root):
            
            
            if not root:
                return 
            
            change(root.right)
            
            
            
            
           
            self.su = self.su + root.val
            
            root.val = self.su
            
            
            change(root.left)
            
            
        
        change(root)
        return root