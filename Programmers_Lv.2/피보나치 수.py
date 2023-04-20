def solution(n):
    a = [0,1]
    for value in range(0,n):
        a.append(a[value]+a[value+1])
    return a[-2]%1234567