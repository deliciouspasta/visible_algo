from tkinter import *
import tkinter as tk
import textbox

class FrameBase(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("800x480")
        self.frame = StartPageFrame(self)
        self.frame.pack(expand = True, fill = "both")

    def change(self,frame):
        self.frame.pack_forget()
        self.frame = frame(self)
        self.frame.pack(expandd = True, fill = "both")

    def backToStart(self):
        self.frame.pack_forget()
        self.frame = StartPageFrame(self)
        self.frame.pack(expand = True,fill = "both")


#class StartPageFrame(tk.Frame):
    







root = tk.Tk()

#ウィンドウサイズ
root.geometry("600x600")

#ウィンドウタイトル
root.title("テスト")

root.configure(background = "blue")

mainFrame = tk.Frame(root,width = 600,height = 2000)
mainFrame.grid(row = 0,column = 0)

mainCanvas = tk.Canvas(
    mainFrame,
    width = 600,
    height = 2000,
    bg = "red",
    scrollregion = (0,0,600,2000)
)


tb1 = textbox.input_box()
tb1.make_box_i(mainCanvas)

tb2 = textbox.input_box()
tb2.make_box_i(mainCanvas)

tb3 = textbox.input_box()
tb3.make_box_i(mainCanvas)

tb4 = textbox.input_box()
tb4.make_box_i(mainCanvas)

tb5 = textbox.input_box()
tb5.make_box_i(mainCanvas)

tb6 = textbox.input_box()
tb6.make_box_i(mainCanvas)



#スクロールバー
vbar = tk.Scrollbar(mainFrame,orient = VERTICAL)
vbar.pack(side = RIGHT,fill = Y)
vbar.config(command = mainCanvas.yview)

mainCanvas.config(width = 600,height = 2000)
mainCanvas.config(yscrollcommand = vbar.set)

mainCanvas.pack(side = LEFT,expand = True,fill = BOTH)





root.mainloop()
