if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    my_list = student_marks[query_name]
    l = len(my_list)
    s = sum(my_list)
    result = s/l
    print("%.2f" % result)

