class Node:
    def __init__(self, data=None, next_node=None) -> None:
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node
        ll_string += " None "
        print(ll_string)
    
    def insert_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
        if self.last_node is None:
            node = self.head
            while node.next_node:
                node = node.next_node
            
            node.next_node = Node(data, None)
            self.last_node = node.next_node
        else:
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node

ll = LinkedList()
node1 = Node("dataN1")
node2 = Node("dataN2", node1)
node3 = Node("dataN3", node2)
node4 = Node("dataN4", node3)
ll.head = node4
ll.print_ll()
ll.insert_beginning("data_new")
ll.print_ll()

