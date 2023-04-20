def solution(ingredient):
    answer = 0
    index = 0
    while index < len(ingredient)-3:
        if ingredient[index] == 1:
            if ingredient[index:index+4] == [1,2,3,1]:
                answer += 1
                del ingredient[index:index+4]
                index = index-3
                continue
        index += 1
    return answer