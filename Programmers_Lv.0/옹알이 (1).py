def solution(babbling):
    answer = 0
    lst = ['aya','ye','woo','ma']
    for value in babbling:
        if len(value) > 10 or len(value) == 1:
            continue
        else:
            while True:
                if value[:2] in lst:
                    value = value[2:]
                elif value[:3] in lst:
                    value = value[3:]
                else:
                    break
            if len(value) == 0:
                answer += 1
    return answer