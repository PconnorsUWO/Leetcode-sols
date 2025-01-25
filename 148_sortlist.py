class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: ListNode) -> ListNode:
    arr=[]
    cur=head
    while cur:
        arr.append(cur.val)
        cur=cur.next
    arr.sort()
    cur=head
    for i in arr:
        cur.val=i
        cur=cur.next
    return head

    values = ll_tolist(head)
    values.sort()
    return list_toll(values)



    
    res = ll_tolist(head).sort()

    def list_toll(res):
        if not res:
            return None
        head = ListNode(res[0])
        cur = head
        for i in range(1, len(res)):
            cur.next = ListNode(res[i])
            cur = cur.next
        return head
    
    return list_toll(res) 

def build_linked_list(data):
    if not data:
        return None
    nodes = [ListNode(x) for x in data]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0] 

def print_linked_list(head):
    if not head:
        return []
    res = []
    cur = head
    while cur:
        res.append(cur.val)
        cur = cur.next
    return res

case1 = [4,2,1,3]
case2 = [-1,5,3,4,0]
head1 = build_linked_list(case1)
head2 = build_linked_list(case2)

print(sortList(head1))