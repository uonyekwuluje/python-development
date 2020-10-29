#!/usr/bin/env python3
import time

unsortedList = [54,26,93,17,77,31,44,55,20]
print(unsortedList)
for x in range(1,len(unsortedList)):
    print("Pass => {}".format(x-1))
    for y in range(0,len(unsortedList)-1):
        if unsortedList[y] > unsortedList[y+1]:
            unsortedList[y],unsortedList[y+1] = unsortedList[y+1],unsortedList[y]
        time.sleep(3)
        print(unsortedList)
