def solution(lottos,win_nums):
    dic = {'6':1,'5':2,'4':3,'3':4,'2':5,'1':6,'0':6}
    ant = 0
    cnt = 0
    for x in lottos:
        if x == 0:
            cnt += 1
        else:
            if x in win_nums:
                continue
            elif x not in win_nums:
                ant += 1
    return [dic[f'{6-ant}'],dic[f'{6-ant-cnt}']]