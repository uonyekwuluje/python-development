#!/usr/bin/env python3
import time

def countdown(n):
    if n == 1:
        return n
    else:
        return n * countdown(n-1)

if __name__ == '__main__':
    num = 5
    print(countdown(num))
