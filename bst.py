# bst.py

from typing import Optional, List
from collections import deque

class TreeNode:
    """
    A binary tree node.
    
    Attributes:
        val (int): The value of the node.
        left (Optional[TreeNode]): The left child.
        right (Optional[TreeNode]): The right child.
    """
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def insert(root: Optional[TreeNode], val: int) -> TreeNode:
    """
    Inserts a value into the BST.
    
    Args:
        root (Optional[TreeNode]): The root of the BST.
        val (int): The value to insert.
    
    Returns:
        TreeNode: The root of the modified BST.
    """
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    
    return root


def search(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Searches for a value in the BST.
    
    Args:
        root (Optional[TreeNode]): The root of the BST.
        val (int): The value to search for.
    
    Returns:
        Optional[TreeNode]: The node with the given value if found, else None.
    """
    if root is None or root.val == val:
        return root
    
    if val < root.val:
        return search(root.left, val)
    else:
        return search(root.right, val)


def inorder(root: Optional[TreeNode]) -> List[int]:
    """
    Performs an inorder traversal of the BST.
    
    Args:
        root (Optional[TreeNode]): The root of the BST.
    
    Returns:
        List[int]: The inorder traversal as a list of values.
    """
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []


def build_tree_from_list(lst: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Builds a binary tree (not necessarily a BST) from a list representing
    the level-order traversal of the tree. `None` indicates missing nodes.
    
    Args:
        lst (List[Optional[int]]): The list of node values.
    
    Returns:
        Optional[TreeNode]: The root of the constructed binary tree.
    
    Example:
        >>> lst = [1, 2, 3, None, 4]
        >>> root = build_tree_from_list(lst)
        >>> # This represents the following tree:
        #       1
        #      / \
        #     2   3
        #      \
        #       4
    """
    if not lst or lst[0] is None:
        return None
    
    root = TreeNode(lst[0])
    queue = deque([root])
    index = 1
    
    while queue and index < len(lst):
        node = queue.popleft()
        
        # Assign left child
        if index < len(lst) and lst[index] is not None:
            node.left = TreeNode(lst[index])
            queue.append(node.left)
        index += 1
        
        # Assign right child
        if index < len(lst) and lst[index] is not None:
            node.right = TreeNode(lst[index])
            queue.append(node.right)
        index += 1
    
    return root


if __name__ == "__main__":
    # Example usage:
    # Build a BST by inserting values.
    values = [5, 3, 7, 2, 4, 6, 8]
    bst_root = None
    for v in values:
        bst_root = insert(bst_root, v)

    print("Inorder traversal of the BST:", inorder(bst_root))
    print("Search for 4:", search(bst_root, 4))

    # Build a tree from a list (level order).
    lst = [1, 2, 3, None, 4]
    tree_root = build_tree_from_list(lst)
    print("Inorder traversal of the built tree:", inorder(tree_root))
