class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def addToFront(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def addToEnd(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def removeFront(self):
        if self.head is None:
            return
        self.head = self.head.next

    def removeEnd(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


linked_list = LinkedList()

linked_list.addToFront(1)
linked_list.addToFront(3)
linked_list.addToFront(2)

linked_list.addToEnd(4)
linked_list.addToEnd(5)
linked_list.addToEnd(6)

print("Linked List Awal : ")
linked_list.printLinkedList()

linked_list.removeFront()
linked_list.removeEnd()

print("Linked List Setelah penghapusan : ")
linked_list.printLinkedList()
