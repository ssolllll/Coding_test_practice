def solution(n):
    answer = []
    while n != 1:
        for value in range(2,n+1):
            if n%value ==0:
                n //= value
                answer.append(value)
                break
    return list(sorted(set(answer)))