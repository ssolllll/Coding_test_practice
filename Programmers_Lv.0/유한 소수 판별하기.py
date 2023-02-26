def solution(a, b):
    c = []
    d = []
    while a != 1:
        for value in range(2,a+1):
            if a%value == 0:
                c.append(value)
                a //= value
    while b != 1:
        for value in range(2,b+1):
            if b%value == 0:
                d.append(value)
                b //= value
                break
    for x in c:
        if x in d:
            d[d.index(x)] = 1
    for y in d:
        if y == 1 or y % 2==0 or y%5==0:
            pass
        else:
            return 2
    return 1