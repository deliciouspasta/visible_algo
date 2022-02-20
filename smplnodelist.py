class Node:
    def __init__(self,value):
        self.value = value
        self.depth = 0
        self.child = None

class Main:
    def __init__(self,value):
        self.cnt = 0
        self.root = Node(value)
        self.printA(value)
        self.printB(value)
        

    def printA(self,value):
        parentNode = self.root
        self.cnt = 10
        child = parentNode.child
        child = Node(value)
        child.depth = self.cnt
        print("A:" + str(child.depth))

    def printB(self,value):
        parentNode = self.root
        self.cnt = 10
        parentNode.child = Node(value)
        parentNode.child.depth = self.cnt
        print("B:" + str(parentNode.child.depth))


obj = Main(100)
  
