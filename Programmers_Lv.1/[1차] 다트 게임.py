def solution(dartResult):
    dic = {'S':1,'D':2,'T':3,'*':2,'#':-1}
    dgt = []
    dgt_alp = ''
    alpha = ''
    for value in dartResult:
        if value.isdigit() == True:
            dgt_alp += value
        else:
            dgt.append(dgt_alp)
            dgt_alp = ''
            alpha += value
    dgt = [x for x in dgt if len(x) != 0]
    alpha = alpha.replace('S', ' S').replace('D', ' D').replace('T', ' T').split(' ')[1:]
    answer = []
    for x,y in enumerate(zip(dgt,alpha)):
        if len(y[1]) != 2:
            answer.append(int(y[0])**dic[y[1]])
        elif len(y[1]) == 2:
            if y[1][1] == '*' and x != 0:
                answer[x-1] = answer[x-1]*2
                answer.append(int(y[0])**dic[y[1][0]]*dic[y[1][1]])
            else:
                answer.append(int(y[0])**dic[y[1][0]]*dic[y[1][1]])
    return sum(answer)