class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def add_node_from_front(self, data):
        """
        1)Create Node from data
        2)Set next of new Node as head Node
        3)Set data of new Node as Head
        :param data:
        :return:
        """
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def remove(self, data):
        """
        1)Start Head
        2)check if data matching
        3)if not search next
        4)Repeat till nodes exits
        :param data:
        :return:
        """
        current_node = self.head
        prev_node = None
        data_found = False
        while not data_found:
            if current_node.get_data() == data:
                data_found = True
            else:
                prev_node = current_node
                current_node = prev_node.get_next()
        if prev_node is None:
            # Data is Head Node
            self.head = current_node.get_next()
        else:
            # Data is other than Head Node
            prev_node.set_next(current_node.get_next())

    def length(self):
        current_node = self.head
        total_nodes = 0
        while current_node is not None:
            current_node = current_node.get_next()
            total_nodes += 1
        return total_nodes

    def search(self, search_data):
        current_node = self.head
        data_found = False
        while current_node is not None and not data_found:
            if current_node.get_data() == search_data:
                data_found = True
            current_node = current_node.get_next()
        return data_found


l1 = LinkedList()
l1.add_node_from_front(1)
l1.add_node_from_front(2)
l1.add_node_from_front(3)
l1.add_node_from_front(4)
print(f"Length :{l1.length()}")
print(f"search 1 :{l1.search(1)}")
l1.remove(1)
print(f"Length :{l1.length()}")
print(f"search 1 :{l1.search(1)}")
