def solution(my_string):
    answer = []
    for v in my_string:
        try:
            answer.append(int(v))
        except:
            continue
    return sorted(answer)