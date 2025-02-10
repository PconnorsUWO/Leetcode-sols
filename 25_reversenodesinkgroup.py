from linkedlist import ListNode

def reverseKGroup(head, k) -> ListNode():
    def reverse(back, front):
        while back != front:
            next_node = back.next
            back.next = front
            front = back
            back = next_node
        return front, back
    dummy = ListNode(0)
    dummy.next = head
    back = dummy
    front = head
    while front:
        count = 0
        while count < k and front:
            front = front.next
            count += 1
        if count == k:
            next_back, next_front = reverse(back.next, front)
            back.next.next = next_front
            back.next = next_back
            back = next_back
            front = next_front
    return dummy.next        
        




# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:
case1 = [1,2,3,4,5]
ll1 = ListNode.build_linked_list(case1)
print(reverseKGroup(ll1, 2))

# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]