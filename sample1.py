import tkinter
import tkinter.ttk as ttk
from tkinter.font import Font

root = tkinter.Tk()

# コンボボックスの作成(rootに配置,リストの値を編集不可(readonly)に設定)
combo = ttk.Combobox(root, state='readonly')
# リストの値を設定
combo["values"] = ("IDを選択","@realDonaldTrump","@justinbieber","@ladygaga","@BarackObama","@katyperry")
# デフォルトの値を食費(index=0)に設定
combo.current(0)
# コンボボックスの配置
combo.grid(column = 0, row = 0, sticky = 'nsew')

#エントリー
EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END,"挿入する文字列")
EditBox.grid(column = 0, row = 1, sticky = 'nsew')

get_b1 = tkinter.Button(root, text = '取得')
get_b1.grid(column = 0, row = 2, sticky = 'nsew')

tw_txt = tkinter.Entry(width=20)
tw_txt.grid(column = 1, row = 1, sticky = 'nsew')

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)

root.mainloop()