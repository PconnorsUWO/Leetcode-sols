class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque

def print_tree(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        if current_node:
            result.append(current_node.val)
            queue.append(current_node.left)
            queue.append(current_node.right)
        else:
            result.append(None)

    return result

def build_tree(nodes):
    if not nodes:
        return None

    root = Node(nodes[0])
    queue = deque([root])
    i = 1

    while i < len(nodes):
        current_node = queue.popleft()

        if nodes[i] is not None:
            current_node.left = Node(nodes[i])
            queue.append(current_node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = Node(nodes[i])
            queue.append(current_node.right)
        i += 1

    return root

def connect(root):
    if not root:
        return None
    
    q = deque([root])
    




# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]

case1 = [1,2,3,4,5,None,7]
tree1 = build_tree(case1) # [1,#,2,3,#,4,5,7,#]
