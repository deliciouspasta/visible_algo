#参考にしたサイト
#https://qiita.com/menon/items/657f67bb2817e25b2222
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 0
        self.direct = ""


class binTree:

    maxdepth = 0

    def __init__(self,mylist):
        self.graph = []
        self.root = None
        for node in mylist:
            self.insert(node)
        self.printGraph(self.root)

    def insert(self,value):

        tmpNode = self.root
        parentNode = None
        self.cnt = 0

        while tmpNode != None:
            parentNode = tmpNode
            if value < tmpNode.value:
                tmpNode = tmpNode.left
                self.cnt += 1
            else:
                tmpNode = tmpNode.right
                self.cnt += 1
        
        binTree.maxdepth = max(binTree.maxdepth,self.cnt)
        
        
        if parentNode == None:
            self.root = Node(value)
            self.root.direct = "root"
            self.graph.append([0,value])
        else:
            if value < parentNode.value:
                parentNode.left = Node(value)     
                parentNode.left.depth = self.cnt
                parentNode.left.direct = "left"
                self.graph.append([parentNode.left.depth,parentNode.left.value])
                
            else:
                parentNode.right = Node(value)
                parentNode.right.depth = self.cnt
                parentNode.right.direct = "right"
                self.graph.append([parentNode.right.depth,parentNode.right.value])
                
    

    def printGraph(self,node):
        std = sorted(self.graph)
        
        j = 0
        for i in range(0,binTree.maxdepth + 1):
            while j < len(std) and i == std[j][0]:        
                print( "\t" + str(std[j][1])+ "\t" ,end="")    
                j += 1
                
            print("\n")
            

    
        
if __name__=="__main__":
    A = [32,75,30,31,65,5,435,4,5,43,523,5,534,5,43,534,5,43,534,5,]
    obj = binTree(A)
    



