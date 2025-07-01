class Stack:
    def __init__(self):
        self.items = []
    #Masukin Data
    def push(self, item):
        self.items.append(item)
    #Keluarin Data
    def pop(self):
        if self.isEmpty():
            print("Stack Kosong")
        self.items.pop()
    # Menampilkan objek terakhir dari stack
    def peek(self):
        return self.items[-1]
    def intip(self):
        if self.isEmpty():
            print("Stack Kosong")
        print(self.items[-1])
	# Memeriksa apakah stack kosong
    def isEmpty(self):
        return self.items == []
	# Menghitung panjang stack
    def size(self):
        return len(self.items)

S = Stack()
S.push("Item 1")
S.push("Item 2")
S.push("Item 3")
print(S.items)
S.pop()
S.pop()
S.pop()
S.pop()
print(S.items)
# S.intip()
# print(S.items)
# print(S.peek())
# print(S.size())
# S.intip()



