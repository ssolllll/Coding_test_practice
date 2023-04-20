def solution(record):
    answer = []
    b = []
    dic = {}
    for i in record:
        a = i
        b.append(a.split())
    for i in range(len(b)):
        try:
            dic[b[i][1]] = b[i][2]
        except:
            pass
    for i in range(len(b)):
        if b[i][0] == "Enter":
            answer.append(f'{dic[b[i][1]]}님이 들어왔습니다.')
        elif b[i][0] == "Leave":
            answer.append(f'{dic[b[i][1]]}님이 나갔습니다.')
    return answer