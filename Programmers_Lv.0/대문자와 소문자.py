def solution(my_string):
    answer =''
    for v in my_string:
        if v.lower() == v:
            answer += v.upper()
        else:
            answer += v.lower()
    return answer