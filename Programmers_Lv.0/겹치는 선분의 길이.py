def solution(lines):
    line = []
    answer = 0
    for x in lines:
        for x1 in range(x[0], x[1]):
            if x1 not in line:
                line.append(x1)
            else:
                line.remove(x1)
                answer += 1
    return answer