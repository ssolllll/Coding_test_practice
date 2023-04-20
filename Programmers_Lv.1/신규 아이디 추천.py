
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
def solution(new_id):
    new_id = new_id.lower() # 1단계
    answer = ''
    for a in new_id: # 2단계
        if a.isalnum() or a in '-_.':
                answer += a
    while answer.count('..') >=1: # 3단계
        answer = answer.replace('..', '.')
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]        # 4단계
    if len(answer) > 0:
        if answer[len(answer)-1] == '.':
            answer = answer[:len(answer)-1]
    if answer == '':
        answer = 'a'# 5단계
    if len(answer) >= 16: # 6단계
        answer = answer[:15]
        if answer[14] == '.':
            answer = answer[:14]
    while len(answer) < 3: # 7단계
        answer += answer[-1]
    return answer