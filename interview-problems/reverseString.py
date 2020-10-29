#!/usr/bin/env python3
# This program takes a string and returns a reversed version of the string
def reverseString1(str1):
    tmpStr = list(str1)
    tmpStr2 = []
    strLen = len(tmpStr)
    for x in range(len(tmpStr),0,-1):
       tmpStr2.append(tmpStr[x-1])
    return "".join(tmpStr2)



if __name__ == '__main__':
    testStr = ["Wiki Land", "hello", "Greetings from Earth"]
    print("Long Version\n..................")
    for x in range(len(testStr)):
        print("Reverse of String {} => [{}]".format(testStr[x], reverseString1(testStr[x])))

    print("\n\nShort Version\n..................")
    for x in range(len(testStr)):
        print("Reverse of String {} => [{}]".format(testStr[x], testStr[x][::-1]))


