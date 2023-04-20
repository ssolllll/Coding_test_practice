def solution(s):
    dic = {}
    for x in set(s):
        dic[x] = -1
    answer = []
    for x,y in enumerate(s):
        if dic[y] == -1:
            answer.append(-1)
            dic[y] = x
        else:
            answer.append(x-dic[y])
            dic[y] = x
    return answer