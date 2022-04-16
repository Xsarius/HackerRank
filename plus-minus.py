import math
import os
import random
import re
import sys

def plusMinus(arr):
    plus = 0
    minus = 0 
    zero = 0
    for i in range(len(arr)):
        if (arr[i] > 0):
            plus += 1
        if (arr[i] < 0):
            minus += 1
        if (arr[i] == 0):
            zero += 1   
    
    print(round(plus/len(arr), 6))
    print(round(minus/len(arr), 6))
    print(round(zero/len(arr), 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
