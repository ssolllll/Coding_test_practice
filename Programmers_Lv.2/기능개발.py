from math import ceil
def solution(p,s):
    answer = []
    b = 0
    for i in range(len(p)):
        if i == 0:
            a = ceil((100-p[i])/s[i])
            b += 1
        elif ceil((100-p[i])/s[i]) <= a:
            b += 1
        elif ceil((100-p[i])/s[i]) > a:
            a = ceil((100-p[i])/s[i])
            answer.append(b)
            b = 1
    answer.append(b)
    return answer