if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks = student_marks.get(query_name)
    avg = float(sum(marks)/len(marks))
    avg = "{:.2f}".format(avg)
    print(avg)
