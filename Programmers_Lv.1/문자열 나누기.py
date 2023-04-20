def solution(s):
    answer = 0
    while len(s) != 0:
        ans = answer
        f_c = 0
        a_c = 0
        ccc = s[0]
        for x,y in enumerate(s):
            if y == ccc:
                f_c += 1
            else:
                a_c += 1
            if f_c == a_c:
                s = s[x+1:]
                answer += 1
                break
        if answer == ans:
            answer += 1
            s = ''
            break
    return answer