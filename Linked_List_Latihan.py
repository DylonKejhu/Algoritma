class Node() :
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head #insert ke kepala
            self.tail.prev = new_node
            self.head = new_node #tambah pergeseran kepala

    def insert_tail(self, data):
        new_node = Node(data)
        if self.head is None or self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail #insert ke ekor
            self.tail.next = new_node
            self.tail = new_node #tambah pergeseran ekor

    def remove_head(self):
        current_head = self.head
        self.head = self.head.next
        self.head.prev = None

        # current_head.next = None
        # current_head = None


    def remove_tail(self):
        current_tail = self.tail
        self.tail = self.tail.prev
        self.tail.next = None

        # current_tail.prev = None
        # current_tail = None

    def remove_node(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                # lakukan penghapusan
                current_node.prev.next = current_node.next
                current_node.next.prev = current_node.prev
                print(data, "removed")
                break
            # optional
            # current_node.next = None
            # current_node.prev = None
        else:
            current_node = current_node.next


    def print_head(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_tail(self):
        current_node = self.tail
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.prev


X = LinkedList()
X.insert_head("Tugas Pertama")
X.insert_head("Tugas Kedua")
X.insert_tail("Tugas Ketiga")
X.remove_head()
X.remove_tail()


print("------------------------")
print("From Head:")
X.print_head()
print("From Tail:")
X.print_tail()