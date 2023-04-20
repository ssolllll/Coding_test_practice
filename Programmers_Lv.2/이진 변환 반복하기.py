def solution(s):
    a = 0
    cnt = 0
    while s != "1":
        a += s.count('0')
        s = bin(len(s.replace("0",'')))[2:]
        cnt += 1
    return [cnt,a]