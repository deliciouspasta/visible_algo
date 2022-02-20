#参考にしたサイト
#https://qiita.com/menon/items/657f67bb2817e25b2222
from transition import TransitionRoutine
from graphviz import Digraph
import tkinter as tk
import sys
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.depth = 0
        self.direct = ""


class binTreeClass(TransitionRoutine):

    maxdepth = 0
    
    #Graphvizを使うときに重複要素を区別するための番号振りに使う
    num = 0

    def __init__(self, master=None, **kwargs):
        super().__init__()
        self.file_opened = TransitionRoutine.file_opened
        if not self.file_opened:
            pass
        else:
            self.graph_img = Digraph(format="png")
            #深さと値の2次元配列
            self.graph = []
            self.pn_str = None
            self.root = None
            for node in self.lines:
                self.insert(node)
            self.printGraph(self.root)

        TransitionRoutine.file_opened = True
        binTreeClass.maxdepth = 0
        binTreeClass.num = 0
        

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
            
        
        binTreeClass.maxdepth = max(binTreeClass.maxdepth,self.cnt)
        
        
        if parentNode == None:
            self.root = Node(value)
            self.root.direct = "root"
            self.graph.append([0,value])
            
            r_str = str(value) + "of" + str(0)
            self.graph_img.node(r_str, str(value))

        else:
            if value < parentNode.value:
                parentNode.left = Node(value)     
                parentNode.left.depth = self.cnt
                parentNode.left.direct = "left"
                self.graph.append([parentNode.left.depth,parentNode.left.value])
                
                self.pn_str = str(parentNode.value) + "of" + str(self.cnt -1)
                n_str = str(value) + "of" + str(self.cnt)
                self.graph_img.node(n_str, str(value))
                self.graph_img.edge(self.pn_str,n_str)
                

                '''
                self.graph_img.node(str(value))
                self.graph_img.edge(str(parentNode.value), str(value))
                '''
                

            else:
                parentNode.right = Node(value)
                parentNode.right.depth = self.cnt
                parentNode.right.direct = "right"
                
                self.graph.append([parentNode.right.depth,parentNode.right.value])
                #値が同じノードの判別のために深さを組み合わせてノードの名前を決定する
                self.pn_str = str(parentNode.value) + "of" + str(self.cnt -1)
                n_str = str(value) + "of" + str(self.cnt)
                self.graph_img.node(n_str, str(value))
                self.graph_img.edge(self.pn_str,n_str)
                

                
                
    

    def printGraph(self,node):
        std = sorted(self.graph)

        scrollbar = tk.Scrollbar(self.frame1)
        scrollbar.pack(side=tk.RIGHT,fill="y")
        txt_widget = tk.Text(self.frame1,width=100,height=600)
    
        
        j = 0
        for i in range(0,binTreeClass.maxdepth + 1):
            txt_widget.insert(tk.END,"深さ＝" + str(i))
            while j < len(std) and i == std[j][0]:          
                txt_widget.insert(tk.END,"\t"*2 + str(std[j][1])+ "\t"+'\n')  
                j += 1

        txt_widget.pack()
        txt_widget["yscrollcommand"] = scrollbar.set

        self.graph_img.render("B2")
        self.graph_img.view()
                
    '''
    def printResult(self):
        scrollbar = tk.Scrollbar(self.frame1)
        scrollbar.pack(side=tk.RIGHT,fill="y")
        txt_widget = tk.Text(self.frame1,width=100,height=600)
        cnt = 0
        for i in self.lines:
            cnt += 1
            txt_widget.insert(tkinter.END,str(cnt)+':\t'+str(i)+'\n')

        txt_widget.pack()
        txt_widget["yscrollcommand"] = scrollbar.set
    '''

    
        
if __name__=="__main__":
    A = [32,75,30,31,65,5,435,4,5,43,523,5,534,5,43,534,5,43,534,5,]
    obj = binTreeClass(A)
    



