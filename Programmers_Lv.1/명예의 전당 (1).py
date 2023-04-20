def solution(k, score):
    answer = []
    lst = []
    for ind in range(1,len(score)+1):
        if k >= ind:
            lst.append(score[ind-1])
            answer.append(min(lst))
        else:
            if min(lst) < score[ind-1]:
                lst[lst.index(min(lst))] = score[ind-1]
                answer.append(min(lst))
            else:
                answer.append(min(lst))
    return answer