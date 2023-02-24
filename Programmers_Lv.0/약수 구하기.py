def solution(n):
    answer = []
    for v in range(1,n+1):
        if n%v == 0:
            answer.append(v)
        else:
            continue
    return answer