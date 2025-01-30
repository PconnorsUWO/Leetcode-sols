class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next
    return head
        

def removeNthFromEnd(head,n):
        dummy = ListNode(0)
        dummy.next = head
        fast = slow = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

