import random

def dataMake(filename):
    with open(filename, mode="w",encoding="utf-8") as f:
        for i in range(0,300):
            num = random.randint(1,10000)
            f.write("{}\n".format(num))

def dataMakeDijk(filename):
    with open(filename, mode="w",encoding="utf-8") as f:
        '''
        for i in range(0,1021):
            num = random.randint(1,100000)
            if i % 6 == 0:
                f.write("\n")
            else:
                f.write("{},".format(num))
        '''

        node_num = random.randint(4,30)
        f.write("{}\n".format(node_num))
        for i in range(node_num):
            for j in range(i + 1):
                f.write("0,")
            for k in range(node_num - i - 1):
                #辺が増えすぎないようにするため、50%でノード間に
                #辺を作らない
                prob_num = random.randint(0,10000)
                dist_num = random.randint(1,300)
                if prob_num < 5000:
                    dist_num = 0
                f.write("{},".format(dist_num))
            f.write("\n")

                

                
            
if __name__ == '__main__' :

    dataMakeDijk("dijkData4to30.txt")
    #dataMake("manyData5.txt")

    print("successed")