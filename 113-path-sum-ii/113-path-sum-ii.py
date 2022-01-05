# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans =[]
        def check(root,target,arr):
            if not root:
                return
            if not root.left and not root.right:
                if target == root.val:
                    ans.append(arr+[root.val])
                    
            return check(root.left,target-root.val,arr+[root.val]) or check(root.right,target-root.val,arr+[root.val])
        
        
        check(root,targetSum,[])
        return ans