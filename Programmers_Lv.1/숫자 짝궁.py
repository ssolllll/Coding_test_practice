def solution(X, Y):
    answer = ''
    lst = [f'{i}' for i in range(9,-1,-1)]
    for i in lst:
        answer += i*(min(X.count(i),Y.count(i)))
    if answer == '':
        return "-1"
    else:
        if len(answer) == answer.count('0'):
            return '0'
        else:
            return answer