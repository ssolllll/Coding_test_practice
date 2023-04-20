def solution(n):
    answer = ""
    a = []
    [a.append(i) for i in list(str(n))]
    for i in sorted(a, reverse=True):
        answer += i
    return int(answer)