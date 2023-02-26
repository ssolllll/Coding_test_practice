def solution(n):
    answer = 0
    value = 1
    while True:
        answer = 0
        for v in range(value,n+1):
            if v%3 == 0 or '3' in str(v):
                answer += 1
        value = n+1
        n += answer
        if answer == 0 and n %3 != 0:
            break
    return n