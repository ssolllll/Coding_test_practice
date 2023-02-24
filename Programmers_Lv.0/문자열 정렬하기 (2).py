def solution(my_string):
    answer = ''
    for v in sorted(my_string.lower()):
        answer += v
    return answer