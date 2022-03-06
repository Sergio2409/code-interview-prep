
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # iterative
    def level_order(_root: Optional[TreeNode]) -> List[List[int]]:
        if not _root:
            return []
        queue = [(_root, 0)]
        res = []
        while queue:
            tmp, level = queue.pop(0)
            res.append([tmp.val]) if len(res) == level else res[level].append(tmp.val)
            if tmp.left:
                queue.append((tmp.left, level+1))
            if tmp.right:
                queue.append((tmp.right, level+1))
            print(res)
        return res

    #recursive
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def traverse(root, level):
            if not root:
                return
            if len(res) == level:
                res.append([root.val])
            else:
                res[level].append(root.val)
            traverse(root.left, level + 1)
            traverse(root.right, level + 1)

        traverse(root, 0)
        return res
