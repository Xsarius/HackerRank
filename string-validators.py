if __name__ == '__main__':
    s = raw_input() 
    
    c1 = False
    c2 = False 
    c3 = False 
    c4 = False 
    c5 = False

    for i in range(len(s)):

        if s[i].isalnum(): c1 = True 
        if s[i].isalpha(): c2 = True
        if s[i].isdigit(): c3 = True 
        if s[i].islower(): c4 = True
        if s[i].isupper(): c5 = True
        
    if c1: print(True)
    else: print(False)
    if c2: print(True)
    else: print(False)
    if c3: print(True)
    else: print(False)
    if c4: print(True)
    else: print(False)
    if c5: print(True)
    else: print(False)