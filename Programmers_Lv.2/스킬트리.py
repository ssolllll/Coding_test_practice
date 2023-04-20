def solution(skill, skill_trees):
    answer = 0
    lst = []
    lst.extend(skill)
    for value in skill_trees:
        a = list(map(lambda x: x if x in lst else '0', value))
        b = ''.join(a).replace('0','')
        if b == '':
            answer += 1
            pass
        else:
            for i,k in zip(skill,b):
                c = 0
                if i != k:
                    c = 1
                    break
                else:
                    pass
            if c == 0:
                answer += 1
    return answer