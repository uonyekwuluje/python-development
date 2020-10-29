#!/usr/bin/env python3
def binarySearch1(lst,item):
    first = 0
    last = len(lst) -1
    isFound = False

    while first <= last and not isFound:
        mid = (first + last)//2
        if lst[mid] == item:
            isFound = True
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1    
    return isFound


def binarySearch2(lst,item):
    first = 0
    last = len(lst) -1
    isFound = False

    while first <= last and not isFound:
        mid = (first + last)//2
        if lst[mid] == item:
            isFound = True
            return str(item) + " found at index "+ str(mid) 
        else:
            if item < lst[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return str(item) + "not found"






if __name__ == '__main__':
    numLst = [5,11,12,17,22,34,46,56,66,78,90,100,150,250]
    print(numLst)
    print(binarySearch1(numLst,22))
    print(binarySearch2(numLst,22))
