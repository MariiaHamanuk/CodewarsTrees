from collections import deque
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Pre-order traversal
def pre_order(node):

    lst = []
    # def real_pre_recurs(node):
    #     if node:
    #         lst.append(node.data)
    #         real_pre_recurs(node.left)
    #         real_pre_recurs(node.right)
    # real_pre_recurs(node)
    
    # return lst
    
    if node:
        stack = deque([node])
        while stack:
            node = stack.pop()
            lst.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return lst
# a = Node(5)
# b = Node(10)
# c = Node(2)
# d = Node("leaf")
# a.left = b
# a.right = c
# c.left = d
# print(pre_order(a))
# In-order traversal
def in_order(node):
    lst = []
    # def real_in_recurs(node):
    #     if node:
    #         real_in_recurs(node.left)
    #         lst.append(node.data)

    #         real_in_recurs(node.right)
    # real_in_recurs(node)
    
    # return lst
    if node:
        stack = deque()
        curr = node
        while stack or curr:
            if curr:
                if  curr not in stack:
                    stack.append(curr)
                if curr.left:
                    stack.append(curr.left)
                curr = curr.left
            else:
                curr = stack.pop()#taking the last element like just returning back up 
                lst.append(curr.data)
                curr = curr.right #checking the other child
        
    return lst
# a = Node(5)
# b = Node(10)
# c = Node(2)
# d = Node("leaf")
# a.left = b
# a.right = c
# c.left = d
# print(in_order(a))
# # Post-order traversal
def post_order(node):
    lst = []
    if node:
        stack = deque([node])
        while stack:
            if stack:
                node = stack.pop()
            lst.append(node.data)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
    lst = lst[::-1]
    return lst
a = Node(5)
b = Node(10)
c = Node(2)
d = Node("leaf")
a.left = b
a.right = c
c.left = d
print(post_order(a))
# Post-order traversal
