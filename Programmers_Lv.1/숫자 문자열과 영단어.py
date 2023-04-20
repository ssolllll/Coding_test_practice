def solution(s):
    str_num = ['zero','one','two','three','four',
               'five','six','seven','eight','nine']
    int_num = [0,1,2,3,4,5,6,7,8,9]
    for st,i in zip(str_num,int_num):
        s = s.replace(st,f'{i}')
    return int(s)