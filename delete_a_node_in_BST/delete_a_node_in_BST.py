# Definition for a binary tree node.
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def tree_by_levels(self, node):
        lst = []

        if node:
            q = deque([node])
            while q:
                curr = q.popleft()
                if curr:
                    lst.append(curr.val)
                    q.append(curr.left)

                    q.append(curr.right)
                else:
                    lst.append(None)

        return lst
    def leftest(self, node):
        while node.left:
            node = node.left
        return node
    def pre_order(self, node, key):
        if not node:
            return None
        if key < node.val:
            node.left = self.pre_order(node.left, key)
        elif key > node.val:
            node.right = self.pre_order(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            min_larger_node = self.leftest(node.right)
            node.val = min_larger_node.val
            node.right = self.pre_order(node.right, min_larger_node.val)
        return node
    def deleteNode(self, root, key):
        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        root2 = self.pre_order(root, key)
        # if not mark:
        #     return root
        # result = self.tree_by_levels(root2)
        return root2
