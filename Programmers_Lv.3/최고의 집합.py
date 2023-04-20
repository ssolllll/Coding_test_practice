def solution(n, s):
    if n > s:
        return [-1]
    elif n == 1:
        return [s]
    answer = [s//n for i in range(n)]
    ind = len(answer) - 1
    for i in range(s - sum(answer)):
        answer[ind] += 1
        ind -= 1
    return answer