# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def su1(root,target):
            
            if not root:
                return False
            
            if not root.right and not root.left and root.val == target:
                return True
            
            target -= root.val
            
            return su1(root.left,target) or su1(root.right,target)
        
        return su1(root,targetSum)
                    
            