def solution(n):
    a = bin(n).count('1')
    while True:
        if a == bin(n+1).count('1'):
            return n+1
        else:
            n = n+1
            continue