#!/usr/bin/env python3
# implementing bubble sort
def bubbleSort(numArray):
    print("Unsorted List => {}".format(sampleDigitList))
    n = len(sampleDigitList)
    for x in range(n):
        for y in range(0,n-x-1):
            if sampleDigitList[y] > sampleDigitList[y+1]:
                sampleDigitList[y], sampleDigitList[y+1] = sampleDigitList[y+1], sampleDigitList[y] 

    print("Sorted List => {}".format(sampleDigitList))



if __name__ == '__main__':
    sampleDigitList = [5,1,4,2,8,3,11,7]
    bubbleSort(sampleDigitList)
