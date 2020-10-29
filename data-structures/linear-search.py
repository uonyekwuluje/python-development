#!/usr/bin/env python3
def linearSearch(lst,item):
    isFound = False
    for x in range(0,len(lst)):
        if item == lst[x]:
           isFound = True
           return "Item found at index " + str(x)
        elif (x == len(lst)-1) and (isFound == False):
           return "Item not found"

if __name__ == '__main__':
    numLst = [11,45,6,8,1,2,9,45,32]
    print(linearSearch(numLst,22))
