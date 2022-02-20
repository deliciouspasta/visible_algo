from transition import TransitionRoutine

class mergeSortClass(TransitionRoutine):
    def __init__(self,master=None,**kwargs):
        super().__init__()
        self.file_opened = TransitionRoutine.file_opened
        if not self.file_opened:
            pass
        else:
            self.mergeSort(0,len(self.lines))
            super().printResult()
        TransitionRoutine.file_opened = True


    def merge(self,left,right):
        mid = (left + right) // 2
        L = self.lines[left:mid]
        R = self.lines[mid:right]
        i = 0
        j = 0

        for k in range(left,right):
            if j == len(R) or i < len(L) and L[i] <= R[j]:
                self.lines[k] = L[i]
                i += 1
            else:
                self.lines[k] = R[j] 
                j += 1

    def mergeSort(self,left,right):
        mid = (left + right) // 2
        if left + 1 < right:
            self.mergeSort(left,mid)
            self.mergeSort(mid ,right)
            self.merge(left,right)

