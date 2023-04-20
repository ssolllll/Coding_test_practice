def solution(today, terms, privacies):
    answer = []
    t = 0
    for day_idx, day in enumerate(today.split('.')):
        if day_idx == 0:
            t += (int(day)-2000)*12*28
        elif day_idx == 1:
            t += (int(day)-1)*28
        else:
            t += int(day)
    term = {f'{t.split()[0]}' : t.split()[1] for t in terms}
    for pri_idx,pri in enumerate(privacies):
        privacies[pri_idx] = privacies[pri_idx][:5]+str(int(privacies[pri_idx][5:7])+int(term[pri[-1]]))+privacies[pri_idx][7:]
    privacies = [pri[:-2].strip() for pri in privacies]
    for pri_idx,pri in enumerate(privacies,start=1):
        v = 0
        for day_idx, day in enumerate(pri.split('.')):
            if day_idx == 0:
                v += (int(day)-2000)*12*28
            elif day_idx == 1:
                v += (int(day)-1)*28
            else:
                v += int(day)
        if t >= v:
            answer.append(pri_idx)
    return answer