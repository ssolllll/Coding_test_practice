def solution(p, c):
    answer = ""
    for x,y in zip(sorted(p), sorted(c)):
        if x != y:
            answer += x
            break
    if answer == "":
        answer += sorted(p)[-1]
    return answer