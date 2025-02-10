class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val) + "->" + str(self.next)
    def __repr__(self):
        return str(self.val) + "->" + str(self.next)
    def build_linked_list(arr):
        head = ListNode(arr[0])
        current = head
        for i in range(1,len(arr)):
            current.next = ListNode(arr[i])
            current = current.next
        return head