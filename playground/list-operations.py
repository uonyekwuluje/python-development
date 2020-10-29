#!/usr/bin/env python3
def list_exp(numLst):
    print(numLst)
    tmp_holding = numLst[-1]

    for x in range(1,len(numLst)):
        numLst[x] = numLst[x-1]
    
    print(numLst)


if __name__ == '__main__':
    nlist = [4,7,1,76,3,6]
    list_exp(nlist)
