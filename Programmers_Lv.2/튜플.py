def solution(s):
    answer = []
    b = s[1:-1].replace('{','').split('}')[:-1]
    for value in sorted(b, key=len):
        for v in value.split(','):
            if v == '':
                pass
            elif v not in answer:
                answer.append(v)
                break
            else:
                pass
    return list(map(lambda x: int(x),answer))