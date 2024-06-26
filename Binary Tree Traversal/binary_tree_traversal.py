"""
Binary tree traversal module in 3 orders
"""

# Pre-order traversal
def pre_order(node) -> list:
    """
    Pre-order tree traversal method
    """
    result = []
    if node:
        result.append(node.data)
        result += pre_order(node.left)
        result += pre_order(node.right)
    return result

# In-order traversal
def in_order(node) -> list:
    """
    In-order tree traversal method
    """
    result = []
    if node:
        result += in_order(node.left)
        result.append(node.data)
        result += in_order(node.right)
    return result

# Post-order traversal
def post_order(node) -> list:
    """
    Post-order tree traversal method
    """
    result = []
    if node:
        result += post_order(node.left)
        result += post_order(node.right)
        result.append(node.data)
    return result