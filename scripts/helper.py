from transition import TransitionRoutine
import tkinter as tk

class helpClass(TransitionRoutine):
    def __init__(self, master=None, **kwargs):
        tk.Frame.__init__(self,master=None, **kwargs)
        self.create_widgets()
        self.printResult()

    def printResult(self):
        scrollbar = tk.Scrollbar(self.frame1)
        scrollbar.pack(side=tk.RIGHT,fill="y")
        self.txt_widget = tk.Text(self.frame1,width=100,height=600)
        self.text_insert()
        self.txt_widget.pack()
        self.txt_widget["yscrollcommand"] = scrollbar.set

    def text_insert(self):
        self.txt_widget.insert(tk.END,"ヘルプ\n\n")
        self.txt_widget.insert(tk.END,
            "実行したいアルゴリズムのアイコンをクリックし、ファイルを選択してください。\n")
        self.txt_widget.insert(tk.END,
            "・ソートとは、大きい順や小さい順などにデータを並び変えることです。\n")
        self.txt_widget.insert(tk.END,
            "・二分探索はソートされたデータでないといけないので注意してください。\n")
        self.txt_widget.insert(tk.END,
            "・二分探索木とダイクストラ法は実行結果がグラフとしても表示されます。\n")
        
