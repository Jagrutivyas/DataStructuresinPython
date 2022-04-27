class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def add_node_to_list(self, new_node):
        print("Adding Node to Linked list")
        temp = self.head
        while temp is not None:
            print(temp.data)
            # print(temp.next)
            print("==========")
            if temp.next is None:
                temp.next = new_node
                break
            temp = temp.next

    def add_value_to_list(self, value):
        print("Adding Value to Linked list")
        new_node = Node(value)
        self.add_node_to_list(new_node)

    def delete_node(self, position):
        print("Deleting Node from Linked list")
        temp = self.head
        i = 1
        while temp is not None:
            if i == position - 1:
                temp.next=temp.next.next
                break
            temp = temp.next
            i += 1


N1 = LinkedList()
N1.head = Node(1)
N2 = Node(2)
N3 = Node(3)
N4 = Node(4)
N1.head.next = N2
N2.next = N3
N3.next = N4
print("Before Adding")
N1.printlist()
N1.add_value_to_list(5)
N6_node = Node(6)
N1.add_node_to_list(N6_node)
print("After Adding")
N1.printlist()
print("Delete 4th postion Node")
N1.delete_node(4)
print("After Delete")
N1.printlist()

