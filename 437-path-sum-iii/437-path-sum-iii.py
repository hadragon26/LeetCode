# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        
        
        def check(node,isRoot,target):
        
        
            if not node:
                return 
            target -= node.val
            if target == 0:
                self.count += 1
                
            check(node.left,False,target)
            check(node.right,False,target)
            
            if isRoot:
                check(node.left,True,targetSum)
                check(node.right,True,targetSum)
        check(root,True,targetSum)
        return self.count
                