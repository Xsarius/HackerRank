import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    
    curr_level = 0
    result = 0
    begin_val = 0
    end_val = 0
    
    for i in range(steps):
        
        temp = curr_level
        
        if(path[i] == 'U'):
            curr_level += 1
        if(path[i] == 'D'):
            curr_level -= 1
        if(temp == 0 and curr_level == -1):
            begin_val = 1
        if(temp == -1 and curr_level == 0):
            end_val = 1
        if(begin_val and end_val == 1):
            begin_val = 0
            end_val = 0
            result += 1
                  
    return result
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
