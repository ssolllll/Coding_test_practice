def solution(clothes):
    dic = {}
    for x in clothes:
        dic[x[0]] = x[1]
    dic1 = {}
    for value in range(len(set(dic.values()))):
        dic1[list(set(dic.values()))[value]] = list(dic.values()).count(list(set(dic.values()))[value])
    answer = 1
    for i in dic1.values():
        answer *= (i+1)
    return answer - 1