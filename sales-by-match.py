import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    
    result = 0
    
    for i in range(1,101):
        x = ar.count(i) / 2
        result += int(x)
          
    return result 
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
 
