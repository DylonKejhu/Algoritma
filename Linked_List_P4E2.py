import time

class Node:
    def __init__(self, data):
        self.next = []
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addnode(self, newdata):
        newnode = Node(newdata)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head
        
    def print(self):
        node = self.head
        while node is not None:
            time.sleep(1)
            print(node.data)
            node = node.next

X = LinkedList()
X.addnode('1')
X.addnode('2')
X.addnode('3')
X.addnode('4')
X.print()





























# node1 = Node('Jl. Zero')
# node2 = Node('Jl. Alpha')
# node3 = Node('Jl. Betta')
# node4 = Node('Jl. Alpha 1')
# node5 = Node('Jl. Alpha 2')
# node6 = Node('Jl. Betta 1')
# node7 = Node('Jl. Betta 2')

# node1.addnext(node2)
# node1.addnext(node3)
# node2.addnext(node4)
# node4.addnext(node5)
# node3.addnext(node6)
# node4.addnext(node7)


# node1.printnodeandnext()