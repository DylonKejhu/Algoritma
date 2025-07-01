class Tree:
    def __init__(self, data):
        self.data = data
        self.next = [None] * 4

    def preorder(self, level = 0):
        print(f"level: {level} Data: {self.data}")
        if self.nevxt[0] != None:
            self.next[0].preorder(level + 1)
        if self.next[1] != None:
            self.next[1].preorder(level + 1)

    def inorder(self, level=0):
        if self.next[0] != None:
            self.next[0].inorder(level + 1)
        print(f"level: {level} Data: {self.data}")
        if self.next[1] != None:
            self.next[1].inorder(level + 1)

    def postorder(self, level=0):
        if self.next[0] != None:
            self.next[0].postorder(level + 1)
        if self.next[1] != None:
            self.next[1].postorder(level + 1)
        print(f"level: {level} Data: {self.data}")

    def depth_first(self):
        stack = [(self, 0)]
        while stack:
            node, level = stack.pop()
            print(f"level: {level} Data: {node.data}")
            if node.next[1] != None:
                stack.append((node.next[1], level + 1))
            if node.next[0] != None:
                stack.append((node.next[0], level + 1))

    def breadth_first(self):
        queue = [(self, 0)]
        index = 0
        while index < len(queue):
            node, level = queue[index]
            print(f"level: {level} Data: {node.data}")
            index += 1
            if node.next[0] != None:
                queue.append((node.next[0], level + 1))
            if node.next[1] != None:
                queue.append((node.next[1], level + 1))

    
print("\nPohon Keluarga")

# Root
root = Tree("Nenek Moyang")
# Kakek Nenek
kakek_ayah = Tree("Kakek Ayah")
nenek_ayah = Tree("Nenek Ayah")
kakek_ibu = Tree("Kakek Ibu")
nenek_ibu = Tree("Nenek Ibu")
# Koneksi Kakek Nenek
root.next[0] = kakek_ayah
root.next[1] = kakek_ibu
# Orang Tua
ayah = Tree("Ayah")
ibu = Tree("Ibu")
# Koneksi Orang Tua
kakek_ayah.next[0] = ayah
nenek_ayah.next[0] = ibu
# Saudara
saya = Tree("Saya")
adik = Tree("Adik")
# Koneksi Saudara
ayah.next[0] = saya
ayah.next[1] = adik
ibu.next[0] = saya
ibu.next[1] = adik

while True:
    print("\nMenu:")
    print("1. Inorder Traversal")
    print("2. Preorder Traversal")
    print("3. Postorder Traversal")
    print("4. Depth-First Traversal")
    print("5. Breadth-First Traversal")
    print("6. Exit")
    
    choice = input("Select an option (1-6): ")
    
    if choice == '1':
        print("\nTree Inorder")
        root.inorder()
    elif choice == '2':
        print("\nTree Preorder")
        root.preorder()
    elif choice == '3':
        print("\nTree Postorder")
        root.postorder()
    elif choice == '4':
        print("\nTree Depth-First")
        root.depth_first()
    elif choice == '5':
        print("\nTree Breadth-First")
        root.breadth_first()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")