def solution(n, numlist):
    answer = []
    for value in numlist:
        if value%n == 0:
            answer.append(value)
        else:
            continue
    return answer