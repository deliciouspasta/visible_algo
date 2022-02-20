from transition import TransitionRoutine

class bubble(TransitionRoutine):
    def __init__(self,master=None,**kwargs):
        super().__init__() 
        self.file_opened = TransitionRoutine.file_opened
        if not self.file_opened:
            pass
        else:
            self.bubbleSort(self.lines)
            super().printResult()
        TransitionRoutine.file_opened = True

    def bubbleSort(self,A):
        N = len(A)
        for i in range(0,N):
            for j in reversed(range(0,N)):
                if j == i:
                    break
                if A[j] < A[j-1]:
                    A[j], A[j-1] = A[j-1], A[j]
