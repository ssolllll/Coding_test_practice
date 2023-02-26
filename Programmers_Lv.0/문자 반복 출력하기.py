def solution(my_string, n):
    answer =''
    for value in my_string:
        answer += value*n
    return answer