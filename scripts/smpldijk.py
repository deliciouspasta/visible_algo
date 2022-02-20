import math

array = [
    [0, 50, 80, 0, 0],
    [0, 0, 20, 15, 0],
    [0, 0, 0, 10, 15],
    [0, 0, 0, 0, 30],
    [0, 0, 0, 0, 0],
    ]

nodeNum = len(array)
unsearchedNode = [i for i in range(nodeNum)]
distance = [math.inf] * nodeNum
priviousNode = [-1] * nodeNum
distance[0] = 0

while len(unsearchedNode) != 0:
    tmpMinDis = math.inf
    tmpMinIndex = -1

    for index in unsearchedNode:
        if tmpMinDis > distance[index]:
            tmpMinDis = distance[index]
            tmpMinIndex = index
    minIndex = tmpMinIndex
    minNode = array[minIndex]
    unsearchedNode.remove(minIndex)

    for index, array_dis in enumerate(minNode):
        if array_dis != 0: 
            if distance[index] > distance[minIndex] + array_dis:
                distance[index] = distance[minIndex] + array_dis
                priviousNode[index] = minIndex
            
print("====経路====")
preNodeNum = nodeNum -1
while preNodeNum != -1:
    if preNodeNum != 0:
        print(str(preNodeNum) + "<-",end="")
    else:
        print(str(preNodeNum))

    preNodeNum = priviousNode[preNodeNum]

print("====距離====")
print(distance[nodeNum - 1])
        
                
                

