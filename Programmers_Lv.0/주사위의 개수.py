def solution(box, n):
    answer = 1
    for v in box:
        answer *= v//n
    return answer