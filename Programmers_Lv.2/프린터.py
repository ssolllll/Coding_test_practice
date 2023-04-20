def solution(p,l):
    b = []
    a = [[value,index]for index,value in enumerate(p)]
    while len(a) >0:
        if a[0][0] == max(a)[0]:
            b.append(a[0])
            a.pop(0)
        else:
            a.append(a[0])
            a.pop(0)
    for x,y in b:
        if y == l:
            return b.index([x,y])+1