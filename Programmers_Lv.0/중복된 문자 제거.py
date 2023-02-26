def solution(my_string):
    answer = []
    for v in my_string:
        if v not in answer:
            answer.append(v)
    c = ''
    for v in answer:
        c += v
    return c