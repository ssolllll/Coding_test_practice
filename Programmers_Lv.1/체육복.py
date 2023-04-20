def solution(n, lost, reserve):
    c = 0
    lst = []
    for l in lost:
        if l in reserve:
            lst.append(l)
    for i in lst:
        lost.pop(lost.index(i))
        reserve.pop(reserve.index(i))
    for k in lost:
        for r in reserve:
            if k-1 == r or k+1 == r:
                c += 1
                reserve.remove(r)
                break
    return n-(len(lost)-c)