import math
import os
import random
import re
import sys

def repeatedString(s, n):
    
    x = s.count('a')
    y = int(n / len(s))
    z = n % len(s)
    q = s.count('a',0,z)
    x *= y
    x += q
    
    return int(x)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
