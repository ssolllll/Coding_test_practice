def solution(score):
    lst = []
    dic = {}
    for value in score:
        lst.append(sum(value)/2)
    for ind,value in enumerate(sorted(lst,reverse=True),start=1):
        if value not in dic:
            dic[value] = ind
    return [dic[value] for value in lst]