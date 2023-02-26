def solution(my_string, letter):
    answer = ''
    for v in my_string:
        if v != letter:
            answer += v
        else:
            continue
    return answer