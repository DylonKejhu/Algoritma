class Ternary:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
    
    def setDataAndChild(self, li):
        mid = len(li) // 2
        self.data = li[mid]
        if(li[:mid] != []):
            print(li[:mid])
            self.left = Ternary()
            self.left.setDataAndChild(li[:mid])
            print("X")
        if(li[mid+1:] != []):
            print(li[mid+1:])
            self.right = Ternary()
            self.right.setDataAndChild(li[mid+1:])
            print("X")

    def inOrderTraversing(self):
        if(self.left != None):
            self.left.inOrderTraversing()
        print(self.data)
        if(self.right != None):
            self.right.inOrderTraversing()

    def preOrderTraversing(self):
        print(self.data)
        if(self.left != None):
            self.left.preOrderTraversing()
        if(self.right != None):
            self.right.preOrderTraversing()

    def postOrderTraversing(self):
        if(self.left != None):
            self.left.postOrderTraversing()
        if(self.right != None):
            self.right.postOrderTraversing()
        print(self.data)

    def search(self, key):
        print("Mencarii..")
        print(self.data)
        if(self.data == key):
            print("Ketemu")
            return True
        elif(self.data > key):
            if(self.left != None):
                print("cari kiri")
                return self.left.search(key)
            else:
                return False
        else:
            if(self.right != None):
                print("cari kanan")
                return self.right.search(key)
            else:    
                return False

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
X = Ternary()
X.setDataAndChild(li)


# print("Inorder Traversing")
# X.inOrderTraversing()
# print("\n")
# print("Preorder Traversing")
# X.preOrderTraversing()
# print("\n")
# print("Postorder Traversing")
# X.postOrderTraversing()

X.search(7)