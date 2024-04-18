"""
Sort binary tree by level module
"""
from collections import deque

def tree_by_levels(node):
    """
    Tree by levels function
    """
    if not node:
        return []

    result = []
    queue = deque([node])

    while queue:
        curr_level = []
        for _ in range(len(queue)):
            curr_node = queue.popleft()
            curr_level.append(curr_node.value)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
        result.extend(curr_level)
    return result
