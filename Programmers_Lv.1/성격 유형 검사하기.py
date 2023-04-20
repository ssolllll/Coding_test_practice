def switch(s, num):
    if num > 4:
        n = 4 - (num - 4)
    elif num < 4:
        n = 4 + (4 - num)
    else:
        return s[1] + s[0], num
    return s[1] + s[0], n


def give_score(num):
    return num - 4


def solution(survey, choices):
    answer = ''
    dic = {}
    lst = ['RT', 'CF', 'JM', 'AN']
    for l in lst:
        dic[f'{l}'] = 0
    for idx, sur in enumerate(survey):
        if sur not in lst:
            sur, choices[idx] = switch(sur, choices[idx])
        num = choices[idx]
        dic[f'{sur}'] += give_score(num)
    for l in lst:
        if dic[f'{l}'] <= 0:
            answer += l[0]
        else:
            answer += l[1]
    return answer