def solution(s):
    answer = 0
    z = []
    for value in s.split(' '):
        if value == 'Z':
            answer -= z[-1]
            del z[-1]
        else:
            answer += int(value)
            z.append(int(value))
    return answer