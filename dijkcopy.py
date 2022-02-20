#参考にしたサイト
#https://qiita.com/shizuma/items/e08a76ab26073b21c207
import math
import tkinter as tk
import os, tkinter, tkinter.filedialog
from transition import TransitionRoutine
from graphviz import Graph

class dijkstraClass(TransitionRoutine):
    def __init__(self,master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.load_resources()
        super().create_widgets()
        self.dijkstra()
        self.printResult()


    def load_resources(self):
        fTyp = [("","*.txt")]

        iDir = os.path.abspath(os.path.dirname(__file__))
        filename = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir = iDir)

        datafile = open(filename,'r')

        self.lines = datafile.readlines()
        self.nodeNum = int(self.lines[0])
    
        #整形された入力データを格納
        self.mylist = [[0]*self.nodeNum for i in range(len(self.lines)-1)]

        for i in range(1,len(self.lines)):
            self.lines[i] = self.lines[i].replace(',\n', '')       
            self.mylist[i-1] = list(self.lines[i].split(','))
            self.mylist[i-1] = list(map(int, self.mylist[i-1]))


    def dijkstra(self):
        #self.nodeNum = len(self.mylist)
        unsearchedNode = [i for i in range(self.nodeNum)]
        
        distance = [math.inf] * self.nodeNum

        #最短経路でそのノードのひとつ前に到達するノードのリスト
        priviousNode = [-1] * self.nodeNum
        distance[0] = 0
        


        while len(unsearchedNode) != 0:
            tmpMinDis = math.inf
            tmpMinIndex = -1

            for index in unsearchedNode:
                if tmpMinDis > distance[index]:
                    tmpMinDis = distance[index]
                    tmpMinIndex = index
            minIndex = tmpMinIndex

            minNode = self.mylist[minIndex]
            unsearchedNode.remove(minIndex)

            #indexは最短距離のノードから
            # 伸びた先のノードの番号を表すことになる（ただし０オリジン）
            for index, mylist_dis in enumerate(minNode):
                if mylist_dis != 0: 
                    if distance[index] > distance[minIndex] + mylist_dis:
                        distance[index] = distance[minIndex] + mylist_dis
                        #ノード'index'の前のノードは'minIndex'　という意味
                        priviousNode[index] = minIndex

        self.priviousNode = priviousNode
        #self.nodeNum = nodeNum
        self.distance = distance

                    

    def printResult(self):

        #最短経路に含まれる辺のリスト(二つのノードで定義)
        self.colored_edges = []
        preNodeNum = self.nodeNum -1

        txt_widget = tk.Text(self.frame1,width=100,height=600)
        txt_widget.insert(tk.END,"========経路========\n")

        while preNodeNum != -1:
            nodeA = preNodeNum + 1
            if preNodeNum != 0:
                txt_widget.insert(tk.END,str(preNodeNum + 1) + "<-")
                
            else:
                txt_widget.insert(tk.END,str(preNodeNum + 1))
                
            preNodeNum = self.priviousNode[preNodeNum]
            nodeB = preNodeNum + 1

            self.nodeAB_append(nodeA, nodeB)

        txt_widget.insert(tk.END,"\n========距離========\n")
        txt_widget.insert(tk.END,self.distance[self.nodeNum - 1])

        txt_widget.pack()

        
        self.print_graph_image()

    def nodeAB_append(self, nodeA, nodeB):
        if nodeA == self.nodeNum:
            nodeA = "g"
        if nodeB == 1:
            nodeB = "s"
        
        if nodeB != 0:
            self.colored_edges.append([str(nodeA), str(nodeB)])
                
    def print_graph_image(self):
        self.graph_img = Graph(format="png")

        #for i in range(1, self.nodeNum + 1):
            #graph_img.node(str(i))
        
        for i in range(self.nodeNum):
            for j in range(self.nodeNum):
                self.graph_maker(i, j)

                   

        self.graph_img.node("s", color="blue")
        self.graph_img.node("g", color="blue")

        for li in self.colored_edges:
            #スタートノード
            if True:
                
                self.graph_img.edge(li[0], li[1], color="green")
                print(li)
                


        self.graph_img.render("dijkImage")
        self.graph_img.view()


    def graph_maker(self, i, j):
        if self.mylist[i][j] != 0:
            if i == 0:
                self.graph_img.edge(
                    "s", 
                    str(j + 1), 
                    label=str(self.mylist[i][j]))

            elif j == self.nodeNum -1: 
                self.graph_img.edge(
                    str(i + 1), 
                    "g", 
                    label=str(self.mylist[i][j]))
            else:
                self.graph_img.edge(
                    str(i + 1), 
                    str(j + 1), 
                    label=str(self.mylist[i][j]))
        
    '''#ダイクストラ実行前の普通のグラフ
    def graph_maker(self, i, j):
        if self.mylist[i][j] != 0:
            if i == 0:
                self.graph_img.edge(
                    "s", 
                    str(j + 1), 
                    label=str(self.mylist[i][j]))

            elif j == self.nodeNum -1: 
                self.graph_img.edge(
                    str(i + 1), 
                    "g", 
                    label=str(self.mylist[i][j]))
            else:
                self.graph_img.edge(
                    str(i + 1), 
                    str(j + 1), 
                    label=str(self.mylist[i][j]))
    '''




    

