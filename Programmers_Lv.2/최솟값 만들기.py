def solution(a,b):
    answer = 0
    a = sorted(a)
    b = sorted(b,reverse=True)
    for x,y in zip(a,b):
        answer += x*y
    return answer