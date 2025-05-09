# node.py

class Node:
    def __init__(self, data):
        self.data = data    # store the value
        self.next = None    # pointer to next node

class LinkedList:
    def __init__(self):
        self.head = None    # start with an empty list

    def append(self, data):
        # add data to the END of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def prepend(self, data):
        # add data to the FRONT of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        # print all items in one line
        curr = self.head
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()

# -------------------------
# example usage

if __name__ == "__main__":
    ll = LinkedList()

    # build list: 10 → 20 → 30
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("After append 10,20,30:")
    ll.print_list()       # prints: 10 20 30

    # add 5 at front: 5 → 10 → 20 → 30
    ll.prepend(5)
    print("After prepend 5:")
    ll.print_list()       # prints: 5 10 20 30

    # add 15 at end: 5 → 10 → 20 → 30 → 15
    ll.append(15)
    print("After append 15:")
    ll.print_list()       # prints: 5 10 20 30 15
