import tkinter as tk
import tkinter.font as font
import os


class CleanUpRoutine(tk.Frame):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)
        self.load_resources()
        self.create_widgets()
        self.n = 0

    def load_resources(self):
        self.base = os.path.dirname(os.path.abspath(__file__))
        self.icon1 = tk.PhotoImage(file=self.base + '/next.png')
        self.icon2 = tk.PhotoImage(file=self.base + '/next_disabled.png')

    def create_widgets(self):
        #Root Setting
        self.master.title("Cleanup Routine")

        #Generate Parts
        frame1 = tk.Frame(master = self)

        quit_button = tk.Button(
            master = frame1,
            command = self.master.backToStart,
            width = 5,
            text = "Back",
            bg = "#00a4e4",
            fg = "#ffffff")

        next_button = tk.Canvas(
            master = self,
            width = 128,
            height = 128)
        self.imagearea = next_button.create_image(
                0, 0, image=self.icon1, anchor=tk.NW)
        next_button.bind("<Button-1>", self.next_clicked)

        self.var = tk.StringVar()
        my_font = font.Font(self,family="Migu 1M",size=20,weight="normal")
        lbl = tk.Label(self, textvariable=self.var, height=5, font=("Migu 1M",20))
        #Layout
        frame1.pack(fill="x")
        quit_button.pack(side="left")
        lbl.pack()
        next_button.pack()

        #Localization
        self.frame1 = frame1
        self.quit_button = quit_button
        self.next_button = next_button
        self.lbl = lbl

    def play(self, filenumber):
        txt = open(self.base + "/wav/CleanupRoutine-" + str(filenumber) + ".txt", 'r', encoding='utf-8')
        self.var.set(txt.read())
        self.master.update()
        txt.close
    
        filename=self.base + "/wav/CleanupRoutine-" + str(filenumber) + ".wav"
        playsound.playAudio(filename)

    def next_clicked(self, event):
        self.next_button.itemconfig(self.imagearea, image = self.icon2)
        self.master.update()
        n = self.n
        self.play(n)
        n = n + 1
        if n > 14:
            n = 0
        self.n = n
        self.next_button.itemconfig(self.imagearea, image = self.icon1)
        self.master.update()