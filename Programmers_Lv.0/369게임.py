def solution(order):
    answer = 0
    clap = ['3','6','9']
    for v in str(order):
        if v in clap:
            answer += 1
    return answer