#!/usr/bin/env python3
# Implementing insertion sort
def insertion_sort(numArray):
    for x in range(1,len(numArray)):
        key = numArray[x]
        position = x
        while position > 0 and numArray[position-1] > key:
            numArray[position] = numArray[position - 1]
            position -= 1
        numArray[position] = key
        print("Pass [{}] => {}".format(x,numArray))




if __name__ == '__main__':
    sampleDigitList = [10,5,9,4,2,8,3,11,7,40,33,16,6]
    print("Unsorted List => {}".format(sampleDigitList))
    insertion_sort(sampleDigitList)
