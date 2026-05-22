# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = [0]
        self.dfs(root, res, float('-inf'))
        return res[0]

    def dfs(self, node, res, max_so_far):
        if not node:
            return
        
        if node.val >= max_so_far:
            res[0] += 1
        
        max_so_far = max(max_so_far, node.val)
        self.dfs(node.left, res, max_so_far)
        self.dfs(node.right, res, max_so_far)

