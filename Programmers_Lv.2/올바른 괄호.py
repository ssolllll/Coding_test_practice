def solution(s):
    while True:
        a = s.find('()')
        if a == 0:
            s = s[2:]
        elif a == -1:
            break
        else:
            s = s[0:a]+s[a+2:]
    if len(s) == 0:
        return True
    else:
        return False