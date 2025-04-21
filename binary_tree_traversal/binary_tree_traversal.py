class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
# Pre-order traversal
def pre_order(node):
    lst = []
    def real_pre_recurs(node):
        if node:
            lst.append(node.data)
            real_pre_recurs(node.left)
            real_pre_recurs(node.right)
    real_pre_recurs(node)
    
    return lst
    
a = Node(5)
b = Node(10)
c = Node(2)
d = Node("leaf")
a.left = b
a.right = c
c.left = d
print(pre_order(a))
# In-order traversal
def in_order(node):
    lst = []
    def real_in_recurs(node):
        if node:
            real_in_recurs(node.left)
            lst.append(node.data)

            real_in_recurs(node.right)
    real_in_recurs(node)
    
    return lst
# Post-order traversal
def post_order(node):
    lst = []
    def real_post_recurs(node):
        if node:
            real_post_recurs(node.left)
            real_post_recurs(node.right)
            lst.append(node.data)


    real_post_recurs(node)
    
    return lst

