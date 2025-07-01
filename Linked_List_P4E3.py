class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.sub = None

tugas1 = Node("Bersih")
tugas2 = Node("Mandi")
tugas3 = Node("Rebahan")
tugas1.next = tugas2
tugas2.next = tugas3

sub1 = Node("Nyapu")
sub2 = Node("Ngepel")
tugas1.sub = sub1
sub1 = Node("Gaming")
sub2 = Node("Berdiam Diri")
sub1.sub = sub2
sub2.sub = tugas3
