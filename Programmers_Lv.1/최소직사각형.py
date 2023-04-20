def solution(sizes):
    a=[]
    b=[]
    for value in sizes:
        a.append(max(value))
        b.append(min(value))
        a = [max(a)]
        b = [max(b)]
    return a[0]*b[0]