# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        lst = []
        
        def rank(root):
            if not root:
                return
            
            if not root.left:
                lst.append(root.val)
            
            
            
            
            rank(root.left)
            
            if root.val not in lst:
                lst.append(root.val)
            
            
            rank(root.right)
            
            
        rank(root)
        
        return lst[k-1]
            