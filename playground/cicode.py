def printList(lstArg):
    print(lstArg)

def stackInplementation():
    print("Stack Implementation\n........................")
    newList = []
    printList(newList)
    newList.append(3)
    printList(newList)
    newList.append(1)
    newList.append(2)
    newList.append(5)
    newList.append(6)
    newList.append(8)
    newList.append(10)
    printList(newList)
    newList.pop()
    newList.pop()
    printList(newList)
    newList.insert(3,25)
    printList(newList)

def queueInplementation():
    print("Queue Implementation\n........................")
    newList = []
    printList(newList)
    newList.append(13)
    newList.append(23)
    newList.append(53)
    printList(newList)
    newList.pop(0)
    printList(newList)
    newList.append(3)
    newList.append(2)
    newList.append(5)
    newList.append(11)
    newList.append(25)
    newList.append(29)
    newList.pop(0)
    printList(newList)



if __name__ == '__main__':
    stackInplementation()
    queueInplementation()
