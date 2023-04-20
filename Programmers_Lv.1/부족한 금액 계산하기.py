def solution(p, m, c):
    answer = p*((c*(c+1)//2))-m
    if answer <=0:
        answer = 0
    return answer