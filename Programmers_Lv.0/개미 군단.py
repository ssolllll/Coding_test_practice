def solution(hp):
    answer = 0
    ant = [ 5,3,1]
    for v in ant:
        answer += hp//v
        hp %= v
    return answer