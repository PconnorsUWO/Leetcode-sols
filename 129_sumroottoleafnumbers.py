class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def construct_tree(data):
    if not data:
        return None
    nodes = [TreeNode(x) if x is not None else None for x in data]
    for i, node in enumerate(nodes):
        if node is None:
            continue
        if 2 * i + 1 < len(nodes):
            node.left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            node.right = nodes[2 * i + 2]
    return nodes[0]
def print_tree(root):
    if not root:
        return []
    res = []
    q = [root]
    while any(q):
        node = q.pop(0)
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    return res

def sumNumbers(root: TreeNode) -> int:
    nums = []

    def dfs(node, num):
        if not node:
            return
        num = num * 10 + node.val
        if not node.left and not node.right:
            nums.append(num)
            return
        dfs(node.left, num)
        dfs(node.right, num)
    
    dfs(root, 0)
    return sum(nums)


case1 = [1,2,3]
case2 = [4,9,0,5,1]
case3 = [1,2,3,4,5,6,7]
root1 = construct_tree(case1)
root2 = construct_tree(case2)
root3 = construct_tree(case3)

print(sumNumbers(root1))
