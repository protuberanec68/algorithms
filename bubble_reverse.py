class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def bubble_sort(self):
        if self.head is None:
            return
            
        sorted_list = False
        while not sorted_list:
            sorted_list = True
            current = self.head
            while current.next is not None:
                if current.data > current.next.data:
                    sorted_list = False
                    temp = current.data
                    current.data = current.next.data
                    current.next.data = temp
                current = current.next

    def reverse(self):
        if self.head is None:
            return

        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

    def print_list(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next

llist = LinkedList()
llist.add(5)
llist.add(3)
llist.add(8)
llist.add(1)
llist.add(2)

print("Before sorting:")
llist.print_list()

llist.bubble_sort()

print("\nAfter sorting:")
llist.print_list()

llist.reverse()

print("\nAfter reversing:")
llist.print_list()