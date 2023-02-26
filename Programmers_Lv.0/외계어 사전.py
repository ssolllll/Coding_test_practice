def solution(spell, dic):
    answer = 2
    for v in dic:
        c = 0
        for k in spell:
            if k in v:
                c += 1
                pass
            else:
                break
        if len(spell) == c:
            return 1
    return 2