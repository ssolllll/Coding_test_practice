def solution(numbers):
    answer = []
    for i in numbers:
        for k in numbers:
            if numbers.index(i) == numbers.index(k):
                if numbers.count(i) >= 2:
                    answer.append(i+k)
                else:
                    pass
            else:
                answer.append(i+k)
    return (list(set(answer)))