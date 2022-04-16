def sort(stud):
    tab = stud
    sol = []
    m = float(101)
    i = 0
    for each in tab:
        if(each[1] < m):
            m = float(each[1])
            i = tab.index(each)
      
    s = len(tab)
    while True:
        if(s == 0):
            break
        if(tab[i][1] == m):
            del tab[i]
        s -= 1
    
    m = float(101)
    
    for each in tab:
        if(each[1] < m):
            m = each[1]
            i = tab.index(each)
    
    for each in tab:
        if(each[1] == m):
            sol.append(each[0])
            
    sol.sort()
    return sol
            
if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    
    sol = sort(students)
    for i in sol:
        print(i)
    
        
