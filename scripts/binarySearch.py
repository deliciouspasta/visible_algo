from mergeSort import mergeSortClass as ms
from transition import TransitionRoutine
import tkinter as tk


class binarySearchClass(TransitionRoutine):
    
    def __init__(self,master=None,**kwargs):
        self.keyValue = -2
        super().__init__()
        self.file_opened = TransitionRoutine.file_opened
        if not self.file_opened:
            pass
        else:
            self.keyInput()
        #print(self.binSearch(0,len(self.lines),self.keyValue))

        TransitionRoutine.file_opened = True

    def binSearch(self,left,right,key):
        key = self.keyValue
        mylist = self.lines
        while left < right:
            mid = (left + right) // 2
            
            if mylist[mid] == key:
                return mid
            elif key < mylist[mid]:
                return self.binSearch(left,mid,key)
            else:
                return self.binSearch(mid+1,right,key)

        return -2

    def keyInput(self):
        
        keyframe = tk.Toplevel()
        keyframe.title("キー入力")
        keyframe.geometry('300x300')
        keyframe.grid()

        lbl = tk.Label(master=keyframe,text='キーを入力してください')
        lbl.grid()

        
        keytxt = tk.Entry(master = keyframe,width=40)
        keytxt.grid()

        self.keyframe = keyframe
        self.keytxt = keytxt    
        
        okButton = tk.Button(
            master = keyframe,
            text = "OK",
            width = 10,
            bg = "#dc143c",
            fg = "#ffffff",
            command = self.getkey
        )
        okButton.grid(column=0,row=2,sticky=tk.NW)
        
    def getkey(self):
        result  = -2
        self.keyValue= int(self.keytxt.get())
        result = self.binSearch(0,len(self.lines),self.keyValue) + 1
        if result < 0:
            txt = str(self.keyValue) + 'は存在しません'
        else:
            txt = str(self.keyValue) + 'は' + str(result) + '行目に存在します'
        lbl = tk.Label(master=self.keyframe,text=txt)
        lbl.grid()
        


    
