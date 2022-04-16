import numpy as np
 
n = input().split()

np.set_printoptions(legacy='1.13')
print (np.eye(int(n[0]), int(n[1])))
