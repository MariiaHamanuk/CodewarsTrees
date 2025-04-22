from collections import deque
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    lst = []
    
    if node:
        q = deque([node])
        while q:
            curr = q.popleft()
            lst.append(curr.value)
            # def recursion(node):
            #     if not node.value in lst:
            #         lst.append(node.value)
            #     if node.left and not node.left.value in lst:
            #         lst.append(node.left.value)
            #     if node.right and not node.right.value in lst:
            #         lst.append(node.right.value)

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

        # recursion(node)
    return lst

# print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)))