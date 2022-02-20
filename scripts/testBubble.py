import random

mylist = [x for x in range(100)]
random.shuffle(mylist)

def bubble():
    length = len(mylist)
    
    for i in range(length):
        for j in reversed(range(i+1, length)):
            if mylist[j-1] < mylist[j]:
                mylist[j-1],mylist[j] = mylist[j], mylist[j-1]
                
bubble()
