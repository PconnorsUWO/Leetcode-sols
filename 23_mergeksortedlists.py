from typing import List, Optional
from collections import deque

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SelfSortingLinkedList:
    def __init__(self):
        self.head = None

    def add(self, node):
        """
        Inserts 'node' into the linked list in ascending order based on 'node.val'.
        Ensures node.next = None before insertion to avoid pointer corruption.
        """
        node.next = None
        
        if not self.head:
            self.head = node
            return

        if node.val < self.head.val:
            node.next = self.head
            self.head = node
            return
        
        cur = self.head
        while cur:
            if not cur.next:
                cur.next = node
                return
            if cur.val <= node.val <= cur.next.val:
                node.next = cur.next
                cur.next = node
                return
            cur = cur.next



def print_linked_list(node):
    while node:
        print(node.val)
        node = node.next

def build_linked_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next
    return head

def mergeKLists(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    sll = SelfSortingLinkedList()
    for l in lists:
        while l:
            new_node = ListNode(l.val)  
            sll.add(new_node)
            l = l.next
    return sll.head

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
case1 = [[1,4,5],[1,3,4],[2,6]]
ll_lists1 = []
for i in case1:
    i = build_linked_list(i)
    ll_lists1.append(i)
print_linked_list(mergeKLists(ll_lists1))
