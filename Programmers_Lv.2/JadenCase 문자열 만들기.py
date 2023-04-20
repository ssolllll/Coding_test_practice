def solution(s):
    answer = ''
    for x,y in enumerate(s):
        if x == 0:
            answer += y.upper()
        elif s[x-1] == " ":
            answer += y.upper()
        else:
            answer += y.lower()
    return answer