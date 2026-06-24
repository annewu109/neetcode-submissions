# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def recur(root, depth):
            if not root:
                return
            if len(res) < depth:
                res.append([])
            res[depth - 1].append(root.val)
            recur(root.left, depth + 1)
            recur(root.right, depth + 1)

        recur(root, 1)
        return res