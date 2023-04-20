def solution(t, p):
    answer = 0
    lst = [t[idx:idx+len(p)] for idx in range(len(t)-len(p)+1)]
    for l in lst:
        if (l <= p) == True:
            answer += 1
    return answer