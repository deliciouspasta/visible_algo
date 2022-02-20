import tkinter as tk
        
keyframe = tk.Toplevel()
keyframe.title("キー入力")
keyframe.geometry('100x200')
keyframe.grid()

lbl = tk.Label(master=keyframe,text='キーを入力してください')
lbl.grid()

keytxt = tk.Entry(master = keyframe,width=40)
keytxt.grid()
keyframe = keyframe
        
        


okButton = tk.Button(
    master = keyframe,
    text = "OK",
    width = 100,
    bg = "#dc143c",
    fg = "#ffffff",
    #command = self.getkey()
)
okButton.grid(column=0,row=2,sticky=tk.NW)


keyframe.mainloop()

