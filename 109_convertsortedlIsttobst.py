from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        while self:
            print(self.val)
            self = self.next
    def build_linked_list(arr):
        head = ListNode(arr[0])
        temp = head
        for i in range(1,len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return head
    
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        copy = []
        while head:
            copy.append(head)
            head = head.next

        def buildBST(l,r):
            if l > r:
                return None
            mid = (l+r)//2
            root = TreeNode(copy[mid].val)
            root.left = buildBST(l,mid-1)
            root.right = buildBST(mid+1,r)
            return root
        return buildBST(0,len(copy)-1)
# Example 1:
# Input: head = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
case1 = [-10,-3,0,5,9]
ll1 = ListNode.build_linked_list(case1)
print(Solution.sortedListToBST(Solution,ll1))

# Example 2:

# Input: head = []
# Output: []