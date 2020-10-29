#!/usr/bin/env python3
# The code computes the factorial of a number
def factorialize1(num):
   fact = 1
   for x in range(num,1,-1):
       fact *= x
   return fact

def factorialize2(num):
   if num == 1:
       return num
   else:
       return num * factorialize2(num-1)



if __name__ == '__main__':
    tNum = [5,10,20,40]
   
    print("Long Version\n................")
    for x in range(len(tNum)):
        print("Factorial of {} = [{}]".format(tNum[x],factorialize1(tNum[x])))

    print("Short Version\n................")
    for x in range(len(tNum)):
        print("Factorial of {} = [{}]".format(tNum[x],factorialize2(tNum[x])))

