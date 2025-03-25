class Node():
    def __init__(self, data = None, prev = None, next = None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

a = Node()
a.data = "SATU"

b = Node()
b.data = "DUA" 
b.prev = a
a.next = b

c = Node()
c.data = "TIGA" 
c.prev = b
b.next = c

a.prev = c
c.next = a

head = a
while head:
    print(head.data)
    head = head.prev