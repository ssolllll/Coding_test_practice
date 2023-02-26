def solution(my_string):
    answer =''
    ahdma = 'aeiou'
    for v in my_string:
        if v in ahdma:
            continue
        else:
            answer += v
    return answer