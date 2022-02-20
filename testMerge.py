import random


mylist = [x for x in range(1000)]
random.shuffle(mylist)


def merge(left, right):
    mid = (left + right) // 2
    l = mylist[left:mid]
    r = mylist[mid:right]
    
    i = j = 0
    
    for k in range(left, right):
        if j == len(r) or i < len(l) and l[i] <= r[j]:
            mylist[k] = l[i]
            i += 1
        else:
            mylist[k] = r[j]
            j += 1
    
    
    
def mergeSort(left, right):
    mid = (left + right) // 2
    if left + 1 < right:
        mergeSort(left, mid)
        mergeSort(mid, right)
        merge(left, right)
    

mergeSort(0,len(mylist))

print(mylist)
