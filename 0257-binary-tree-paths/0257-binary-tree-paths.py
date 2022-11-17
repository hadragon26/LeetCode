# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        
        ans = []
        
        def dfs(root,lst):
            if not root:
                return 
            if not root.left and not root.right:
                lst1 = lst[:]
                lst1.append(str(root.val))
                ans.append((lst1))
                #print(ans)
                return
            lst1 = lst[:]
            lst1.append(str(root.val))
            dfs(root.left,lst1)
            dfs(root.right,lst1)
            
        dfs(root,[])
        final =[]
        for an in ans:
            final.append('->'.join(an))
        return final
            
            