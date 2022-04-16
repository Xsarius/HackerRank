import numpy as np

if __name__ == '__main__':
    n = input().split()
    x = []
    for i in range(len(n)):
        x.append(int(n[i]))
        
    zer = np.zeros(x, dtype = int)
    on = np.ones(x, dtype = int)
    print(zer)
    print(on) 
