# https://www.reddit.com/r/learnpython/comments/776kd9/tkinterhow_can_i_destroyhide_the_root_window/

import tkinter as tk
import tkinter.font as font
import os, tkinter, tkinter.filedialog


class TransitionRoutine(tk.Frame):

    #この変数はアプリ起動中は一連の処理が終わった後にTrueに戻しておかないと
    #前の値が保存されたままになってしまう
    file_opened = True

    def __init__(self,master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.load_resources()
        self.create_widgets()
        self.n = 0

    def load_resources(self):
        '''self.base = os.path.dirname(os.path.abspath(__file__))
        self.icon1 = tk.PhotoImage(file=self.base + '\A1.png')
        self.icon2 = tk.PhotoImage(file=self.base + '\A3.png')'''
        fTyp = [("","*.txt")]

        iDir = os.path.abspath(os.path.dirname(__file__))
        filename = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

        #ファイル選択でキャンセルが押された場合
        if filename == "":
            TransitionRoutine.file_opened = False
            return

        datafile = open(filename,'r')

        self.lines = datafile.readlines()

        for i in range(0,len(self.lines)):
            #行番号付きファイルを読み込むときは以下の一行をコメントから外す
            #self.lines[i].lstrip(str(i+1) + ':\t')
            self.lines[i] = int ( self.lines[i].replace('\n','') )

        print("yeah! succeed!!")

        

#画面遷移によりできたウィンドウ（ウィジェット）のタイトルバーのタイトル
    def create_widgets(self):
        #Root Setting
        self.master.title("Transition_create_widgets Routine")

        #Generate Parts
        frame1 = tk.Frame(master = self)

        quit_button = tk.Button(
            master = frame1,
            command = self.master.backToStart,
            width = 5,
            text = "Back",
            bg = "#00a4e4",
            fg = "#ffffff")

        '''
        next_button = tk.Canvas(
            master = self,
            width = 300,
            height = 300)
        self.imagearea = next_button.create_image(
                0, 0, image=self.icon1, anchor=tk.NW)
        next_button.bind("<Button-1>", self.next_clicked)'''

        self.var = tk.StringVar()
        my_font = font.Font(self,family="Migu 1M",size=20,weight="normal")
        lbl = tk.Label(self, textvariable=self.var, height=5, font=("Migu 1M",20))
        #Layout
        frame1.pack(fill="x")
        quit_button.pack(side="left")
        lbl.pack()
        #next_button.pack()

        #Localization
        self.frame1 = frame1
        self.quit_button = quit_button
        #self.next_button = next_button
        self.lbl = lbl
        

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
        with open("sortedData3-1.txt",mode="w",encoding="utf-8") as f:
            for i in self.lines:
                f.write("{}\n".format(i))
        '''
        
        

    
    '''
    def next_clicked(self, event):
        self.next_button.itemconfig(self.imagearea, image = self.icon2)
        self.master.update()
        n = self.n
        n = n + 1
        if n > 14:
            n = 0
        self.n = n
        self.next_button.itemconfig(self.imagearea, image = self.icon1)
        self.master.update()
    '''

