class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_data_first(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insert_data_last(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return
        tmp = self.head
        while (tmp.next):
            tmp = tmp.next
        tmp.next = new_node

    def insert_data_custom(self, prev_node, new_data):
        if prev_node is None:
            print('ops!! enter a real prev node,your prev node is not exists!')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def traverse(self):
        tmp = self.head
        while (tmp):
            print(tmp.data)
            tmp = tmp.next

my_linked_list=Linked_list()

my_linked_list.head=Node('data1')

second_node=Node('data2')
my_linked_list.head.next=second_node

third_node=Node(3)
second_node.next=third_node

my_linked_list.insert_data_custom(second_node,4)
my_linked_list.traverse()