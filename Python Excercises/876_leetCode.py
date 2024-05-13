def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    id = 0
    temp = head
    while temp.next is not None:
        id += 1
        temp = temp.next
