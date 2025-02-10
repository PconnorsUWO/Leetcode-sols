from linkedlist import ListNode

def swapPairs(head):
    """
    :type head: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    def swap(back, front):
        back.val, front.val = front.val, back.val
        
    temp = head
    while temp and temp.next:
        swap(temp, temp.next)
        temp = temp.next.next
    return head

case1= [1,2,3,4]
case2= []
case3= [1]
case4= [1,2,3]
ll1 = ListNode.build_linked_list(case1)

print(swapPairs(ll1))
# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:

# Example 2:

# Input: head = []

# Output: []

# Example 3:

# Input: head = [1]

# Output: [1]

# Example 4:

# Input: head = [1,2,3]

# Output: [2,1,3]