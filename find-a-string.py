def count_substring(string, sub_string):
    
    x = []

    [x.append(i) for i in range(len(string)) if string.startswith(sub_string, i)]
    
    return len(x)
    
    

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count