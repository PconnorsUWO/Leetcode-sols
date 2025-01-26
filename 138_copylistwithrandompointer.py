class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
def build_linked_list(data):
    if not data:
        return None
    nodes = [Node(x[0]) for x in data]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, random_index) in enumerate(data):
        if random_index is not None:
            nodes[i].random = nodes[random_index]
    return nodes[0] 


def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    cur = head
    if cur.random == None:
        cur = cur.next()


data = [[7, None], [13, 0], [11, 4], [10, 2], [1, None]]
head = build_linked_list(data)
print(copyRandomList(head))