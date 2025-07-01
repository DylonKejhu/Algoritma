class Node:
    def __init__(self, data):
        self.next = []
        self.data = data

    def addnext(self,newNode):
        self.next.append(newNode)

    def printnodeandnext(self, pos = 1):
        print(pos,': ', self.data)
        pos += 1
        for nextNode in self.next:
            nextNode.printnodeandnext(pos)


# Create root node
main = Node("Main")

# Create first path: Road Alpha → Road Alpha 1
road_alpha = Node("Road Alpha")
road_alpha_1 = Node("Road Alpha 1")
road_alpha.addnext(road_alpha_1)

# Create second path: Road Betta → Road Betta 1
road_betta = Node("Road Betta")
road_betta_1 = Node("Road Betta 1")
road_betta.addnext(road_betta_1)

# Add Road Alpha and Road Betta to Main
main.addnext(road_alpha)
main.addnext(road_betta)

# ===== Print structure =====
main.printnodeandnext()