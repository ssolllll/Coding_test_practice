def solution(balls, share):
    answer = balls
    for value in range(balls-1,balls-share,-1):
        answer *= value
    for k in range(share,0,-1):
        answer //= k
    return answer