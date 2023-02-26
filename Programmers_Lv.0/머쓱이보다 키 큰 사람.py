def solution(array, height):
    answer = 0
    for value in array:
        if height < value:
            answer += 1
    return answer