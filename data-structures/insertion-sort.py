#!/usr/bin/env python3
import time

def tmpTestMove(strLst,index):
    print(strLst)
    temp = strLst[index]
    for x in range(index,0,-1):
        strLst[x] = strLst[x-1]
    unsortedList[0] = temp
    print(strLst)

#def insertSort(strLst):
#    print(strLst)
#    for index in range(1, len(strLst)):
#        current = strLst[index]
#        position = index
#
#        while position > 0 and strLst[position-1] > current:
#            print("Swapped {} for {}".format(strLst[position], strLst[position-1]))
#            strLst[position] = strLst[position-1]
#            print(strLst)
#            position -= 1
#
#        strLst[position] = current
#    print(strLst)



def insertSort(strLst):
    print(strLst)
    for index in range(1, len(strLst)):
        current = strLst[index]
        position = index

        while position > 0 and strLst[position-1] > current:
            strLst[position] = strLst[position-1]
            position -= 1

        strLst[position] = current
    print(strLst)


  


if __name__ == '__main__':
    unsortedList = [54,26,93,17,77,31,44,55,20]
    insertSort(unsortedList)
