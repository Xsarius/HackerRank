import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    temp = arr
    temp.sort()
    minimum = 0
    maximum = 0
    for i in range(1,5):
        minimum += temp[i - 1]
        maximum += temp[-1*i]
    print(minimum, maximum)    
    

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
