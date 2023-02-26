def solution(p):
    p = p.split('+')
    num = 0
    x = 0
    for value in p:
        try:
            num += int(value)
        except:
            value = value.strip()
            try:
                x += int(value[:-1])
            except:
                x += 1
    if num == 0:
        if x == 1:
            return f'x'
        else:
            return f'{x}x'
    elif x == 0:
        return f'{num}'
    else:
        if x == 1:
            return f'x + {num}'
        else:
            return f'{x}x + {num}'