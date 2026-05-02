# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check(self, root, SubRoot):
        if root is None or SubRoot is None:
            if root is not None or SubRoot is not None:
                return False
        if root is None and SubRoot is None:
            return True
        if root.val==SubRoot.val:
            return self.check(root.left, SubRoot.left) and self.check(root.right, SubRoot.right)
        else:
            return False

    def dfs(self, root, SubRoot):
        if root is None:
            return False
        if root.val==SubRoot.val:
            a = self.check(root,SubRoot)
            if a:
                return True
        return self.dfs(root.left, SubRoot) or self.dfs(root.right, SubRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root, subRoot)



