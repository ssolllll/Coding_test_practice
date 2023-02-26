def solution(n):
    answer = []
    for v in range(n+1):
        if v%2 != 0:
            answer.append(v)
    return answer