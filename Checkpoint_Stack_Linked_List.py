class LinkedListStack:
    def __init__(self):
        self.top = None  # Menunjuk ke elemen teratas stack

    def push(self, data):
        new_node = Node(data)  # Buat node baru
        new_node.next = self.top  # Node baru menunjuk ke node teratas saat ini
        self.top = new_node  # Update node teratas menjadi node baru

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        popped_node = self.top  # Ambil node teratas
        self.top = self.top.next  # Update node teratas ke node berikutnya
        return popped_node.data  # Kembalikan data dari node yang dihapus

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        return self.top.data  # Kembalikan data dari node teratas

    def is_empty(self):
        return self.top is None  # Cek apakah stack kosong

# Contoh penggunaan
stack = LinkedListStack()
stack.push("Checkpoint 1")
stack.push("Checkpoint 2")
stack.push("Checkpoint 3")

print("Top element:", stack.peek())  # Output: Top element: Checkpoint 3
print("Popped element:", stack.pop())  # Output: Popped element: Checkpoint 3
print("Top element after pop:", stack.peek())  # Output: Top element after pop: Checkpoint 2
