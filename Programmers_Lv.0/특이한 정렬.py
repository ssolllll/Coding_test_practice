def solution(numlist, n):
    answer = sorted([abs(n-i) for i in numlist])
    lst = []
    for ind in range(len(answer)-1):
        if ind+1 <= len(lst):
            continue
        elif answer[ind] == answer[ind+1]:
            lst.append(n+answer[ind])
            lst.append(n-answer[ind])
        else:
            if n+answer[ind] in numlist:
                lst.append(n+answer[ind])
            elif n-answer[ind] in numlist:
                lst.append(n-answer[ind])
    if n+answer[-1] in numlist:
        lst.append(n+answer[-1])
    else:
        lst.append(n-answer[-1])
    return lst