def solution(k, m, score):
    answer = 0
    if len(score) < m:
        return 0
    c = 0
    for num in range(k,-1,-1):
        a = c//m
        c += score.count(num)
        if a != c//m:
            answer += ((c//m)-a)*num*m
    return answer