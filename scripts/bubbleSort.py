


def bubbleSort(A):
    N = len(A)
    for i in range(0,N):
        for j in reversed(range(0,N)):
            if j == i:
                break
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


A = [133 , 3213, 32333, 4343, 876]

 
bubbleSort(A)

print(A)



