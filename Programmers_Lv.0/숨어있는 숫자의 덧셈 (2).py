def solution(my_string):
    answer = 0
    c = ''
    for value in my_string:
        try:
            int(value)
            c += value
        except:
            try:
                answer += int(c)
                c = ''
            except:
                c = ''
                continue
    try:
        answer += int(c)
    except:
        return answer
    return answer