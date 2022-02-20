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
        self.print_result()


    def load_resources(self):
        fTyp = [("","*.txt")]

        iDir = os.path.abspath(os.path.dirname(__file__))
        filename = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir = iDir)

        datafile = open(filename,'r')

        self.lines = datafile.readlines()
        self.nodeNum = int(self.lines[0])
    
        #整形された入力データを格納するリスト
        self.graph_list = [[0]*self.nodeNum for i in range(self.nodeNum)]

        for i in range(1,len(self.lines)):
            self.lines[i] = self.lines[i].replace(',\n', '')       
            self.graph_list[i-1] = list(self.lines[i].split(','))
            self.graph_list[i-1] = list(map(int, self.graph_list[i-1]))


    def dijkstra(self):
        #self.nodeNum = len(self.graph_list)
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

            minNode = self.graph_list[minIndex]
            unsearchedNode.remove(minIndex)

            #indexは最短距離のノードから
            # 伸びた先のノードの番号を表すことになる（ただし０オリジン）
            for index, graph_list_dis in enumerate(minNode):
                if graph_list_dis != 0: 
                    if distance[index] > distance[minIndex] + graph_list_dis:
                        distance[index] = distance[minIndex] + graph_list_dis
                        #ノード'index'の前のノードは'minIndex'　という意味
                        priviousNode[index] = minIndex

        self.priviousNode = priviousNode
        #self.nodeNum = nodeNum
        self.distance = distance

                    
    #文字列として実行結果を示す関数。
    def print_result(self):

        #グラフ描画の際に用いる。最短経路の一部の辺をred,それ以外の辺をblackとする。
        self.color_edges = [["black"]*self.nodeNum for i in range(self.nodeNum)]
        
        preNodeNum = self.nodeNum -1

        txt_widget = tk.Text(self.frame1,width=100,height=600)
        txt_widget.insert(tk.END,"========経路========\n")

        while preNodeNum != -1:
            nodeA = preNodeNum
            if preNodeNum != 0:
                txt_widget.insert(tk.END,str(preNodeNum + 1) + "<-")
                    
            else:
                txt_widget.insert(tk.END,str(preNodeNum + 1))
                
            preNodeNum = self.priviousNode[preNodeNum]
            nodeB = preNodeNum

            if nodeB != -1:
                self.color_edges[nodeB][nodeA] = "red"

        txt_widget.insert(tk.END,"\n========距離========\n")
        txt_widget.insert(tk.END,self.distance[self.nodeNum - 1])
        txt_widget.pack()
     
        self.print_graph_image()


    #結果のグラフの描画
    def print_graph_image(self):
        self.graph_img = Graph(format="png")

        for i in range(self.nodeNum):
            for j in range(self.nodeNum):
                self.graph_maker(i, j)
                  
        self.graph_img.node("s(1)", color="blue")
        self.graph_img.node("g(" + str(self.nodeNum) + ")", color="blue")
            
        self.graph_img.render("dijkImage")
        self.graph_img.view()

    #最短経路を赤線で、それ以外を黒線でノード同士をつなぐ関数
    def graph_maker(self, i, j):
        if self.graph_list[i][j] != 0:
            if i == 0:
                self.graph_img.edge(
                    "s(1)", 
                    str(j + 1), 
                    label=str(self.graph_list[i][j]),
                    color=self.color_edges[i][j])

            elif j == self.nodeNum -1: 
                self.graph_img.edge(
                    str(i + 1), 
                    "g(" + str(j + 1) + ")", 
                    label=str(self.graph_list[i][j]),
                    color=self.color_edges[i][j])
            else:
                self.graph_img.edge(
                    str(i + 1), 
                    str(j + 1), 
                    label=str(self.graph_list[i][j]),
                    color=self.color_edges[i][j])
        
    '''#ダイクストラ実行前の普通のグラフ
    def graph_maker(self, i, j):
        if self.graph_list[i][j] != 0:
            if i == 0:
                self.graph_img.edge(
                    "s", 
                    str(j + 1), 
                    label=str(self.graph_list[i][j]))

            elif j == self.nodeNum -1: 
                self.graph_img.edge(
                    str(i + 1), 
                    "g", 
                    label=str(self.graph_list[i][j]))
            else:
                self.graph_img.edge(
                    str(i + 1), 
                    str(j + 1), 
                    label=str(self.graph_list[i][j]))
    '''




    

