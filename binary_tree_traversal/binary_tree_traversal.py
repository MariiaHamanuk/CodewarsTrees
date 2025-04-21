# Pre-order traversal
def pre_order(node):
    lst  = []
    if node:
        lst.append(node.data)
        pre_order(node.left)
        pre_order(node.right)
        
    return lst

# In-order traversal
def in_order(node):
    return []

# Post-order traversal
def post_order(node):
    return []

