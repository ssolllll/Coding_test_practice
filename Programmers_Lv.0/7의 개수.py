def solution(array):
    answer = 0
    for v in array:
        for k in str(v):
            if k == '7':
                answer += 1
    return answer