def solution(quiz):
    answer = []
    for value in quiz:
        value = value.split()
        if value[1] == '-':
            if int(value[0])-int(value[2]) == int(value[4]):
                answer.append('O')
            else:
                answer.append('X')
        else:
            if int(value[0]) + int(value[2]) == int(value[4]):
                answer.append('O')
            else:
                answer.append('X')
    return answer