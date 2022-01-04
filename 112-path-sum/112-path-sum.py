# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def check(target,root):
            if not root:
                return False
            if not root.left and not root.right:
                if target == root.val:
                    return True
                else:
                    return False
            
            return check(target-root.val,root.left) or check(target-root.val,root.right)
            
            
        return check(targetSum,root)
        
        
        
            
                    
            