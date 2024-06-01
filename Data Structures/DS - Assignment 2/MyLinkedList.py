# submissionId=1274085814

class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def addAtTail(self, val):
        temp = self.head
        if temp is None:
            self.head = Node(val)
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = Node(val)
        self.size += 1

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            node = Node(val)
            node.next = temp.next
            temp.next = node
            self.size += 1

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        temp = self.head
        if index == 0:
            self.head = temp.next
        else:
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
        self.size -= 1