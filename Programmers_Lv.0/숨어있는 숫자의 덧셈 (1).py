def solution(my_string):
    answer = 0
    for v in my_string:
        try:
            answer += int(v)
        except:
            continue
    return answer