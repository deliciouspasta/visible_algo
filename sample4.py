import tkinter as tk

def test():
    global canvasT
    global root

    textT = ''
    for i in range(0,100):
        textT = textT + 'test' + str(i) + '\n'
    canvasT.create_text(5, 5, text = textT, width = 760, anchor = tk.NW)
    canvasT.configure(scrollregion=(0,0,761,1500))

def run():

    global canvasT
    root = tk.Tk()
    root.geometry("800x600")

    frame = tk.Frame(root)
    frame.place(x=10,y=10)
    canvasT = tk.Canvas(frame, width =761, height = 550, bd = 1,
                       relief = tk.SUNKEN, bg = 'white')
    sb = tk.Scrollbar(frame, orient = tk.VERTICAL, command = canvasT.yview)
    canvasT.configure(yscrollcommand = sb.set)
    canvasT.grid(row = 0, column = 0, sticky = tk.NW)   
    sb.grid(row = 0, column = 1, sticky = tk.NS)

    button = tk.Button(frame, text = "test", command = test)
    button.grid(row = 1, column = 0, sticky = tk.NW) 


    root.mainloop()

if __name__ == '__main__':
    run()