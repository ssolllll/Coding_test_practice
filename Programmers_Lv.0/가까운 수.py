def solution(array, n):
    for v,k in enumerate(array):
        if v == 0:
            answer = k
        elif abs(n-answer) == abs(n-k):
            if answer > k:
                answer = k
        elif abs(n-answer) > abs(n-k):
            answer = k
    return answer