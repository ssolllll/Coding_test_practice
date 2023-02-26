def solution(n):
    i = 0
    c = 1
    while True:
        i += 1
        c *= i
        if n == c*(i+1):
            i += 1
            break
        elif n < c*(i+1):
            break
    return i