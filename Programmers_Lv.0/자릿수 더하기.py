def solution(n):
    answer = 0
    for v in str(n):
        answer += int(v)
    return answer