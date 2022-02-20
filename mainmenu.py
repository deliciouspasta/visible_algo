#参考にしたサイト
# https://www.reddit.com/r/learnpython/comments/776kd9/tkinterhow_can_i_destroyhide_the_root_window/
import tkinter as tk
from bubbleExe import bubble
from mergeSort import mergeSortClass
from binarySearch import binarySearchClass
from binTree import binTreeClass
from dijkstra import dijkstraClass
from transition import TransitionRoutine
from helper import helpClass
from dummy import DummyApp
class FrameBase(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x480")
        self.frame = StartPageFrame(self)
        self.frame.pack(expand=True, fill="both")
        #self.attributes("-fullscreen", True)

    def change(self, frame):
        self.frame.pack_forget() # delete currrent frame
        #キャストではなくただの関数の呼び出しによるオブジェクトの代入
        #self.StartPageFrame(self)=TransitionRoutine(Applist[r][c][0])↓?
        #つまりはself.frame = TransitionRoutine(Applist[r][c][0])ということ？↓
        self.frame = frame(self)
        self.frame.pack(expand=True, fill="both") # make new frame

    def backToStart(self):
        self.frame.pack_forget()
        self.frame = StartPageFrame(self)
        self.frame.pack(expand=True, fill="both")

class StartPageFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        master.title("Start Page")

        self.grid(column=0, row=0, sticky=tk.NSEW)

        self.Applist = [
                    [ [bubble, "バブルソート"], [mergeSortClass, "マージソート"],[binarySearchClass, "二分探索"] ], 
                    [[binTreeClass, "二分探索木"],[dijkstraClass, "ダイクストラ法"],[helpClass, "ヘルプ"] ]
                    ]

        lbl = tk.Label(master=self, text ="Start Page", font=("Migu 1M",14))
        lbl.grid(column=0,row=0,sticky=tk.NW, padx=10)
        btn = tk.Button(
            master = self,
            text="Close",
            width = 5,
            bg = "#dc143c",
            fg = "#ffffff",
            command=self.master.destroy)
        btn.grid(column=2, row=0,sticky=tk.NE)

        for r in range(1,3):
            for c in range(3):
                btn = tk.Button(
                        master=self,
                        wraplength=150,
                        justify=tk.LEFT,
                        text=self.Applist[r-1][c][1],
                        font=("Migu 1M", 32),
                        bg="#00ff7f",
                        command=self.gotoApp(r-1,c))
                btn.grid(column=c, row=r, padx=10, pady=10, sticky=tk.NSEW)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def gotoApp(self,r,c):
        return lambda :self.master.change(self.Applist[r][c][0])

if __name__=="__main__":
    app=FrameBase()
    app.mainloop()