def solution(before, after):
    answer = 1
    for v in set(before):
        if before.count(v) == after.count(v):
            continue
        else:
            return 0
    return answer