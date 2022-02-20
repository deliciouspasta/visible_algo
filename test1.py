import tkinter as tk

class App(tk.Frame):
    def __init__(self,txt,master=None):
        tk.Frame.__init__(self, master)
        a=tk.Frame(master)
        tk.Label(a,text=txt).pack(side=tk.LEFT)
        tk.Button(a,text="Push").pack(side=tk.LEFT)
        a.pack()

root=tk.Tk()
b=App("AAA",master=root)
c=App("BBB",master=b)
b.pack()
c.pack()
root.mainloop()